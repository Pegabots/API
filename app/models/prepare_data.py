"""
   Classe de preparação dos arquivos para elaboração do conjunto de treinamento para os métodos de aprendizagem de máquina,
   reunindo informações de diferentes arquivos, bem como a extração de dados para o mesmo formato do modelo gerado quando 
   da aplicação em um novo perfil
"""

import pandas as pd
import numpy as np
import statistics

class MLTools:

    def prepare_data(self, df_users, df_timeline, path_trendtopics_data = "app/models/trending_topics.csv", verbose = False):
        """
            Método principal de extração/reunião de informaões para o conjunto de treinamento ou do novo perfil a ser avaliado
            Os parâmetros são:
            df_users: dados básicos dos usuários do conjunto de treinamento
            df_timeline: dados referentes às últimas postagens dos usuários do treinamento
            path_trendtopics_data: caminho do arquivo (CSV) contendo o monitoramento de trending topics
            verbose: opção de exibir informações da geração do modelo (default: False)

            O método retorna um DataFrame X contendo o conjunto de dados preparados para ser recebido pelo modelo
        """

        df_users = df_users.fillna(0)
        df_users['É bot?'] = ''

        #Extrai as informações de retweet
        if not('tweet_is_retweet' in df_timeline.columns and 'tweet_text' in df_timeline.columns):
            raise Exception("Problems on tweets")
        
        df_timeline['retweet_tratado'] = df_timeline['tweet_is_retweet'].apply(lambda x: "sim" if (x == 'True' or x == True) else "não")
        df_timeline['tweet_com_rt_tratado'] = df_timeline['tweet_text'].apply(lambda x: "sim" if x.find("RT @") != -1 else "não" )

        def reune_rt(retweet,rt):
            if retweet == 'sim' or rt == 'sim':
                return 'sim'
            else:
                return 'não'
        df_timeline['retweet_e_tweet_com_rt_tratado'] = df_timeline.apply(lambda x: reune_rt(x.retweet_tratado, x.tweet_com_rt_tratado), axis=1)

        #Calcula o tempo médio e mínimo entre os tweets do usuário
        #Incluir uma dedida da distancia temporal entre twittes (mediana e mínimo)
        df_users['Tempo mediano'] = np.array(len(df_users))
        df_users['Tempo menor']   = np.array(len(df_users))
        iuser = 0
        for user in df_users['handle']:
            df_temp = df_timeline[df_timeline['tweet_author'] == user]
            itweet = 0
            menor = 100000
            difs = list()
            tweet_date_prev = None
            for tweet in df_temp['tweet_created_at']:
                tweet_date = pd.to_datetime(pd.to_datetime(tweet).strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                if itweet > 0:
                    dif = (tweet_date_prev - tweet_date).seconds
                    if dif < menor:
                        menor = dif
                    difs.append(dif)
                else:
                    tweet_date_prev = tweet_date
                tweet_date_prev = tweet_date
                itweet += 1
            if len(difs) > 0:
                mediana = statistics.median(difs)
            else:
                mediana = 1000
            if verbose:    
                print(user + ' - ' + str(menor) + ' - ' + str(mediana)+'\n')
            df_users['Tempo mediano'][iuser] = mediana
            df_users['Tempo menor'][iuser]   = menor
            iuser += 1

        #Reune os dados básicos do usuário com o agrupamento da timeline e classificação alvo
        df_result_text = df_timeline.groupby('tweet_author').agg({'tweet_text':lambda col: ', '.join(col)}).reset_index()
        df_result_hashtags = df_timeline.groupby('tweet_author').agg({'tweet_hashtags':lambda col: ', '.join(col)}).reset_index()
        df_result_source = df_timeline.groupby('tweet_author').agg({'tweet_source':lambda col: ', '.join(col)}).reset_index()
        df_result_retweet = df_timeline.groupby('tweet_author').agg({'retweet_tratado':lambda col: ', '.join(col)}).reset_index()
        df_result_tweet_com_rt = df_timeline.groupby('tweet_author').agg({'tweet_com_rt_tratado':lambda col: ', '.join(col)}).reset_index()
        df_result_retweet_e_tweet_com_rt = df_timeline.groupby('tweet_author').agg({'retweet_e_tweet_com_rt_tratado':lambda col: ', '.join(col)}).reset_index()


        #Reune os dados (merge) do usuários, suas avaliações com texto dos tweets, as hashtags, as fontes e os retweets
        df_result_merge = df_users
        df_result_merge = pd.merge(df_result_merge,df_result_text, left_on=['handle'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_hashtags, left_on=['handle'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_source, left_on=['handle'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_retweet, left_on=['handle'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_tweet_com_rt, left_on=['handle'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_retweet_e_tweet_com_rt, left_on=['handle'], right_on=['tweet_author'])

        #Padroniza a saída da classificação do INCT-DD para bot e monta o conjunto Y
        #Caso outro padrão de classificação seja adotado na planilha, deve-se alterar AQUI
        df = df_result_merge

        #Monta o conjunto de treinamento
        feature_cols = ['twitter_followers_count', 'twitter_friends_count', 'Tempo mediano', 'Tempo menor']
        x = df[feature_cols]

        qtd_hashtags = df['tweet_hashtags'].apply(lambda x: len(x.replace("[","").replace("]","").replace(", \'","$").split("$")))
        x['Quantidade hashtags'] = np.array(list(qtd_hashtags))
        qtd_hashtags_media = df['tweet_hashtags'].apply(lambda x: len(x.replace("[","").replace("]","").replace(", \'","$").split("$"))/len(x.split(", [")))
        x['Quantidade hashtags media'] = np.array(list(qtd_hashtags_media))

        #Inclui o número de dígitos no nome
        username_digitos = df['handle'].apply(lambda x: sum(c.isdigit() for c in str(x)) ) #handle ou tweet_author
        x['Digitos no username'] = np.array(list(username_digitos))

        #O tamanho do nome e do login
        tam_username = df['handle'].apply(lambda x: len(str(x)))
        tam_nome = df['twitter_user_name'].apply(lambda x: len(str(x)))
        x['Tamanho do username'] = np.array(list(tam_username))
        x['Tamanho do nome'] = np.array(list(tam_nome))

        #Calcula a quantidade de twittes por diferentes fontes
        fonte_android = df['tweet_source'].apply(lambda x: str(x).count('Twitter for Android') )
        fonte_iphone = df['tweet_source'].apply(lambda x: str(x).count('Twitter for iPhone') )
        fonte_web = df['tweet_source'].apply(lambda x: str(x).count('Twitter Web App') )

        fonte_soma = fonte_android + fonte_iphone + fonte_web
        fonte_soma = fonte_soma.apply(lambda x: 1 if x <= 0 else x )

        #Calcula o percentual por usuário
        fonte_android = fonte_android/fonte_soma
        fonte_iphone = fonte_iphone/fonte_soma
        fonte_web = fonte_web/fonte_soma

        x['Fonte de Android'] = np.array(list(fonte_android))
        x['Fonte de iPhone'] = np.array(list(fonte_iphone))
        x['Fonte de Web'] = np.array(list(fonte_web))
        x = x.fillna(0)

        retweet_tratado = df['retweet_tratado'].apply(lambda x: str(x).count('sim')/len(x.split(",")))
        x['retweet_tratado_media'] = np.array(list(retweet_tratado))

        tweet_com_rt = df['tweet_com_rt_tratado'].apply(lambda x: str(x).count('sim')/len(x.split(",")))
        x['tweet_com_rt_tratado_media'] = np.array(list(tweet_com_rt))

        retweet_e_tweet_com_rt = df['retweet_e_tweet_com_rt_tratado'].apply(lambda x: str(x).count('sim')/len(x.split(",")))
        x['retweet_e_tweet_com_rt_tratado_media'] = np.array(list(retweet_e_tweet_com_rt))

        x_novo = x
        x_novo.shape

        #Inclui informações das trend topics
        #Busca os dados de todas as trending topics recuperadas
        datafile_trends = path_trendtopics_data
        df_trends = pd.read_csv(datafile_trends, header = 0)
        #Preenche os valores NaN con 0 apenas para avaliação geral
        df_trends = df_trends.fillna(0)

        #Inclui um percentual de trending topics utilizado por tweet
        #Para tweet, busca pelos trending topics imediatamente anteriores
        df_timeline['Numero de trendings'] = np.array(len(df_timeline))
        df_timeline['Numero de trendings'] = 0
        df_trends['Trend Date Time Convertido'] = np.array(len(df_trends))
        itrend = 0
        for x in df_trends['trend_date_time']:
            df_trends['Trend Date Time Convertido'][itrend] = pd.to_datetime(x).strftime("%Y-%m-%d")
            itrend += 1

        itweet = 0
        for tweet in df_timeline['tweet_created_at']:
            tweet_date = pd.to_datetime(pd.to_datetime(tweet).strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
            df_temp = df_trends[df_trends['Trend Date Time Convertido'] == tweet_date.strftime("%Y-%m-%d")] #.strftime("%Y-%m-%d")]
            
            itrend = 0
            for trend in df_temp['Trend Date Time Convertido']:
                trend_date = pd.to_datetime(pd.to_datetime(trend).strftime("%Y-%m-%d"))
                if trend_date <= tweet_date.tz_convert(None):
                    if df_timeline['tweet_text'][itweet].find(df_trends['trend'][itrend]) != -1: 
                        df_timeline['Numero de trendings'][itweet] = df_timeline['Numero de trendings'][itweet] + 1
                itrend += 1
            if verbose:    
                print("Search trend topics: " + str((itweet/len(df_timeline['tweet_created_at'])*100)) + "%")
            itweet += 1     

        #Reune as informações de trends nos tweets por author
        df_result_trend = df_timeline.groupby('tweet_author').agg({'Numero de trendings':lambda col: sum(col)/len(col)}).reset_index()
        df_result_trend_max = df_timeline.groupby('tweet_author').agg({'Numero de trendings':lambda col: max(col)}).reset_index()
        df_result_trend['trends_media'] = df_result_trend['Numero de trendings']
        df_result_trend_max['trends_max'] = df_result_trend_max['Numero de trendings']

        #Retira os tópicos repetidos
        trends_unique = df_trends.trend.unique()

        df_result_merge = pd.merge(df_result_merge,df_result_trend, left_on=['handle'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_trend_max, left_on=['handle'], right_on=['tweet_author'])

        df_result_merge['qtdtrends'] = np.array(list(tam_username))
        ttemp = 0
        iuser = 0
        for user in df_result_merge.tweet_text:
            for trend in trends_unique:
                if user.find(trend) != -1:
                    ttemp = ttemp + 1
            if verbose:    
                print(str(ttemp) + " - " + str(iuser) + " | " + str((iuser/len(df_result_merge.tweet_text))*100) + "%")
            df_result_merge['qtdtrends'][iuser] = ttemp
            iuser = iuser + 1
            ttemp = 0

        x_novo_trend = x_novo

        x_novo_trend['qtdtrends'] = df_result_merge['qtdtrends']
        x_novo_trend['trends_media'] = df_result_merge['trends_media']
        x_novo_trend['trends_max'] = df_result_merge['trends_max']

        return x_novo_trend