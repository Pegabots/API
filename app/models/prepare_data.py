"""
   Classe de preparação dos arquivos para elaboração do conjunto de treinamento para os métodos de aprendizagem de máquina,
   reunindo informações de diferentes arquivos, bem como a extração de dados para o mesmo formato do modelo gerado quando 
   da aplicação em um novo perfil
   
   Versão: 2.0.0 / 2a atualização dos modelos do Pegabot via aprendizagem de máquina
"""

#Carrega as bibliotecas / Load libraries
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestRegressor
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import tree
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, matthews_corrcoef, mean_squared_error, r2_score, mean_absolute_percentage_error, max_error, explained_variance_score, median_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier, GradientBoostingClassifier
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report
import math
import statistics
import datetime
import pytz
import pickle
import textdistance


class PegaBotTools:

    def prepare_data(self, dataset_users, dataset_timeline, dataset_paths_analyses = "", apply = False, verbose = False):
        """
            Método principal de extração/reunião de informaões para o conjunto de treinamento ou do novo perfil a ser avaliado
            Os parâmetros são:
            dataset_paths_users: caminho do arquivo (CSV) contendo os dados básicos dos usuários do conjunto de treinamento
            dataset_paths_analyses: caminho do arquivo (CSV) dados de classificação final desses usuários (bots/não)
            dataset_paths_timeline: caminho do arquivo (CSV) contendo as últimas postagens dos usuários do treinamento
            apply: indica se a preparação é para aplicação do modelo (não existe dados previamente avaliados - dataset_paths_analyses)
            verbose: opção de exibir informações da geração do modelo (default: False)

            O método retorna dois resultados quando de treinamento (apply = False):
                DataFrame x contendo o conjunto X de treinamento
                DataFrame y contendo os rótulos do conjunto de treinamento

            Ou apenas o DataFrame X no caso de aplicação
        """

        #Load user data for training
        df_users = dataset_users

        #Remove line with "api_erros" from data source
        #df_users = pd.read_csv(datafile_users, header = 0, on_bad_lines = 'skip', sep = ';')
        df_users = df_users.fillna(0)


        #Load label (target) from users (only for training)
        if not apply:
            path_target_data = dataset_paths_analyses
            datafile_handles = path_target_data
            df_target = pd.read_csv(datafile_handles, header = 0, sep = ',')

        #Load timeline data from users
        df_timeline = dataset_timeline
        
        # Start preprocessing
        #Extract retweet information
        #First, if the current tweet was retweeted by other user
        df_timeline['timeline_retweeted'] = df_timeline['tweet_retweeted'].apply(lambda x: "yes" if (x == 'True' or x == True) else "no")

        #Second, if the current tweet is a quote from other tweet
        df_timeline['timeline_quote'] = df_timeline['tweet_is_quote'].apply(lambda x: "yes" if (x == 'True' or x == True) else "no")

        #Finally, if the current tweet is a simple (pure) retweet from other tweet (no text included over the original tweet)
        df_timeline['timeline_pureretweet'] = df_timeline['tweet_text'].apply(lambda x: "yes" if x.find("RT @") != -1 else "no" )


        #Join pure retweet with quote
        def join_retweet(retweet,rt):
            if retweet == 'yes' or rt == 'yes':
                return 'yes'
            else:
                return 'no'                
        df_timeline['timeline_quote_and_pureretweet'] = df_timeline.apply(lambda x: join_retweet(x.timeline_pureretweet, x.timeline_quote), axis=1)

        #Calc temporal distance between tweets
        #Include median, min, max, stdev and mean about tweet create time
        df_users['timeline_median'] = np.array(len(df_users))
        df_users['timeline_min']   = np.array(len(df_users))
        df_users['timeline_stdev']   = np.array(len(df_users))
        df_users['timeline_max']   = np.array(len(df_users))
        df_users['timeline_mean']   = np.array(len(df_users))
        iuser = 0
        for user in df_users['id']:
            df_temp = df_timeline[df_timeline['tweet_author_id'] == user]
            itweet = 0
            menor = 100000
            maior = 0
            difs = list()
            tweet_date_prev = None
            for tweet in df_temp['tweet_created_at']:
                tweet_date = pd.to_datetime(pd.to_datetime(tweet).strftime("%Y-%m-%dT%H:%M:%S.%fZ"))
                if itweet > 0:
                    dif = (tweet_date_prev - tweet_date).seconds
                    if dif < menor:
                        menor = dif
                    if dif > maior:
                        maior = dif
                    difs.append(dif)
                else:
                    tweet_date_prev = tweet_date
                tweet_date_prev = tweet_date
                itweet += 1
            if len(difs) > 0:
                mediana = statistics.median(difs)
                stdev = statistics.stdev(difs)
                media = statistics.mean(difs)
            else:
                mediana = 1000
                media = 1000
                stdev   = 0
                
            if verbose:
                print(str(user) + ' - ' + str(menor) + ' - ' + str(mediana)+'\n')
                
            df_users['timeline_median'][iuser] = mediana
            df_users['timeline_min'][iuser]   = menor
            df_users['timeline_stdev'][iuser]   = stdev
            df_users['timeline_max']   = maior
            df_users['timeline_mean']   = media
            iuser += 1
            
        #Grouping timeline data by user
        df_result_text = df_timeline.groupby('tweet_author').agg({'tweet_text':lambda col: ', '.join(col)}).reset_index()
        df_result_hashtags = df_timeline.groupby('tweet_author').agg({'tweet_hashtags':lambda col: ', '.join(col)}).reset_index()
        df_result_source = df_timeline.groupby('tweet_author').agg({'tweet_source':lambda col: ', '.join(col)}).reset_index()
        df_result_reply = df_timeline.groupby('tweet_author').agg({'in_reply_to_status_id':lambda col: ', '.join(col)}).reset_index()
        df_result_retweeted = df_timeline.groupby('tweet_author').agg({'timeline_retweeted':lambda col: ', '.join(col)}).reset_index()
        df_result_pureretweet = df_timeline.groupby('tweet_author').agg({'timeline_pureretweet':lambda col: ', '.join(col)}).reset_index()
        df_result_quote = df_timeline.groupby('tweet_author').agg({'timeline_quote':lambda col: ', '.join(col)}).reset_index()
        df_result_quote_and_pureretweet = df_timeline.groupby('tweet_author').agg({'timeline_quote_and_pureretweet':lambda col: ', '.join(col)}).reset_index()


        #Merge basic user data with the grouped timeline data
        if not apply:
            df_result_merge = pd.merge(df_target, df_users, left_on=['handle'], right_on=['handle'])
        else:
            df_result_merge = df_users

        if verbose:
            print(df_result_merge)
            
        #Merge user data with tweet, hashtags, sources and reteweets
        df_result_merge = pd.merge(df_result_merge, df_users, left_on=['handle'], right_on=['handle'])
        df_result_merge = pd.merge(df_result_merge,df_result_text, left_on=['handle'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_hashtags, left_on=['tweet_author'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_source, left_on=['tweet_author'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_reply, left_on=['tweet_author'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_retweeted, left_on=['tweet_author'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_pureretweet, left_on=['tweet_author'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_quote, left_on=['tweet_author'], right_on=['tweet_author'])
        df_result_merge = pd.merge(df_result_merge,df_result_quote_and_pureretweet, left_on=['tweet_author'], right_on=['tweet_author'])

        #Extract new features from collected data
        df_result_new_features = df_result_merge
        
        #Creation time in days
        from datetime import datetime, date, timezone
        date_format = "%Y-%m-%d %H:%M:%S%z" #2009-06-30 01:05:51+00:00
        df_result_new_features['created_at_x']

        now = datetime.now(timezone.utc)
        difdate = df_result_new_features['created_at_x'].apply(lambda x: ( now - datetime.strptime(x, date_format)).days ) 
        df_result_new_features['user_creation_lifetime_in_days'] = difdate
        
        #Number of the hashtags
        qtd_hashtags = df_result_new_features['tweet_hashtags'].apply(lambda x: len(x.replace("[","").replace("]","").replace(", \'","$").split("$")))
        df_result_new_features['timeline_hashtags_number'] = np.array(list(qtd_hashtags))
        qtd_hashtags_media = df_result_new_features['tweet_hashtags'].apply(lambda x: len(x.replace("[","").replace("]","").replace(", \'","$").split("$"))/len(x.split(", [")))
        df_result_new_features['timeline_hashtags_number_mean'] = np.array(list(qtd_hashtags_media))
        
        #Number of digits on the username
        username_digits = df_result_new_features['tweet_author'].apply(lambda x: sum(c.isdigit() for c in str(x)) ) 
        df_result_new_features['user_digits_on_name'] = np.array(list(username_digits))
        
        #Length of the name and username (handle)
        len_username = df_result_new_features['tweet_author'].apply(lambda x: len(str(x)))
        len_name = df_result_new_features['name_x'].apply(lambda x: len(str(x)))
        df_result_new_features['user_length_username'] = np.array(list(len_username))
        df_result_new_features['user_length_name'] = np.array(list(len_name))       
        
        #Legnth of the description account
        len_description = df_result_new_features['description_y'].apply(lambda x: len(str(x)))
        df_result_new_features['user_length_description'] = np.array(list(len_description))
        
        #Identify sources of the tweets
        source_android = df_result_new_features['tweet_source'].apply(lambda x: str(x).count('Twitter for Android') )
        source_iphone = df_result_new_features['tweet_source'].apply(lambda x: str(x).count('Twitter for iPhone') )
        source_web = df_result_new_features['tweet_source'].apply(lambda x: str(x).count('Twitter Web App') ) + df_result_new_features['tweet_source'].apply(lambda x: str(x).count('Twitter Web Client') )

        def calcSourceAPI(x):
            textos = x.split(',')
            web = 0
            iphone = 0
            android = 0
            outros = 0
            for i in textos:
                if i.strip() == 'Twitter for Android':
                    android += 1
                elif i.strip() == 'Twitter for iPhone':
                    iphone += 1
                elif i.strip() == 'Twitter Web App' or  i == 'Twitter Web Client':
                    web += 1
                else:
                    outros += 1            
            return outros

        def calcSourceNamedBot(x):
           textos = x.split(',')
           tbot = 0
           for i in textos:
               if 'BOT' in i.upper():
                   tbot += 1
           return tbot
            
        source_other = df_result_new_features['tweet_source'].apply(lambda x:calcSourceAPI(x))
        source_bot =  df_result_new_features['tweet_source'].apply(lambda x:calcSourceNamedBot(x))
       
        #Verify number of tweets with source
        source_sum = source_android + source_iphone + source_web + source_other
        source_sum = source_sum.apply(lambda x: 1 if x <= 0 else x )
       
        #Insert source rate
        source_android = source_android/source_sum
        source_iphone = source_iphone/source_sum
        source_web = source_web/source_sum
        source_other = source_other/source_sum
        source_bot = source_bot/source_sum

        df_result_new_features['timeline_source_android'] = np.array(list(source_android))
        df_result_new_features['timeline_source_iphone'] = np.array(list(source_iphone))
        df_result_new_features['timeline_source_web'] = np.array(list(source_web))
        df_result_new_features['timeline_source_other'] = np.array(list(source_other))
        df_result_new_features['timeline_source_botname'] = np.array(list(source_bot))
       
        #Calc number of replies
        def calcReplyPosts(x):
           textos = x.split(',')
           reply = 0
           for i in textos:
               if 'NONE' not in i.upper():
                   reply += 1
           return reply

        timeline_reply = df_result_new_features['in_reply_to_status_id'].apply(lambda x:calcSourceAPI(x))
        df_result_new_features['timeline_replies_count'] = np.array(list(timeline_reply))       
       
        #Calc retweet, quote and retweeted rate (and pure retweet plus quote)
        retweeted_mean = df_result_new_features['timeline_retweeted'].apply(lambda x: str(x).count('yes')/len(x.split(",")))
        df_result_new_features['timeline_retweeted_mean'] = np.array(list(retweeted_mean))

        quote_mean = df_result_new_features['timeline_quote'].apply(lambda x: str(x).count('yes')/len(x.split(",")))
        df_result_new_features['timeline_quote_mean'] = np.array(list(quote_mean))

        pureretweet_mean = df_result_new_features['timeline_pureretweet'].apply(lambda x: str(x).count('yes')/len(x.split(",")))
        df_result_new_features['timeline_pureretweet_mean'] = np.array(list(pureretweet_mean))

        quote_and_pureretweet_mean = df_result_new_features['timeline_quote_and_pureretweet'].apply(lambda x: str(x).count('yes')/len(x.split(",")))
        df_result_new_features['timeline_quote_and_pureretweet_mean'] = np.array(list(quote_and_pureretweet_mean))      
       
        #Calc relation between number of tweets and account time in days
        tweets_by_accountlifetime = df_result_new_features['statuses_count_y']/df_result_new_features['user_creation_lifetime_in_days']
        df_result_new_features['user_tweets_by_accountlifetime'] = tweets_by_accountlifetime      
       
        #Calc relation between number of tweets and likes
        likes_by_tweets = df_result_new_features['favourites_count_x']/df_result_new_features['statuses_count_y']
        df_result_new_features['user_likes_by_tweets'] = likes_by_tweets      
       
        #Calc relation between number of replies and tweets
        replies_by_tweets = df_result_new_features['timeline_replies_count']/df_result_new_features['statuses_count_y']
        df_result_new_features['timeline_replies_by_tweets'] = replies_by_tweets       

        #Calc mean distance between a tweet and its predecessor
        def calcDistanceTextTweets(x):
          textos = x.split(',')
          distance_sum = 0
          #for i in textos:
          for i in range(1, len(textos)):
              str1 = str(textos[i])
              str2 = str(textos[i-1])
              #Only to user text
              if (str1.find("RT @") == -1) and (str2.find("RT @") == -1):
                  dist = textdistance.levenshtein.distance(str1,str2)
              elif (str1.find("RT @") == -1):
                  dist = textdistance.levenshtein.distance(str1,'')
              elif (str2.find("RT @") == -1):
                  dist = textdistance.levenshtein.distance('',str2)
              else:
                  dist = 0
          return dist/len(textos)

        timeline_textdistance = df_result_new_features['tweet_text'].apply(lambda x:calcDistanceTextTweets(x))
        df_result_new_features['timeline_textdistance'] = np.array(list(timeline_textdistance))       
      
        if verbose:
          print(df_result_new_features.columns)
          
        #Extract X and y values to training
      
        df = df_result_new_features
        #Define unique labels (1 - Bot, 0 - No bot)
        if not apply:
           #Input label from column "É bot" - to application this column is empty
           y = df['É Bot?'].apply(lambda x: 1 if (x == 'Sim' or x == 'sim') else 0)
           y.reset_index(drop=True, inplace=True)
          
        #Select features to training
        feature_cols = ['user_creation_lifetime_in_days', 'timeline_hashtags_number', 'timeline_hashtags_number_mean', 
                'user_digits_on_name', 'user_length_username', 'user_length_name', 'timeline_source_iphone', 
                'timeline_source_web', 'timeline_source_other', 'timeline_source_botname', 
                'timeline_retweeted_mean', 'timeline_quote_mean', 'timeline_pureretweet_mean', 
                'timeline_quote_and_pureretweet_mean', 'favourites_count_x', 'followers_count_x', 'statuses_count_x',
                'friends_count_x', 'verified_x', 'timeline_median_x', 'timeline_min_x', 'timeline_stdev_x', 
                'timeline_max_x', 'timeline_mean_x', 'user_tweets_by_accountlifetime', 
                'user_likes_by_tweets', 'timeline_replies_count', 
                'timeline_replies_by_tweets', 'timeline_textdistance']
        x = df[feature_cols]     
    
        x = x.fillna(0)
        x.replace([np.inf, -np.inf], 0, inplace=True)    
      
        if not apply: 
           return x, y
        else:
           return x
