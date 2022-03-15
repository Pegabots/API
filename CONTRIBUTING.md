
# Contribuindo para o projeto

Olá! Obrigado pelo interesse em contribuir com essa API. Esse repositório implementa a API do Pegabot, capaz de buscar dados por meio da API do Twitter e solicitar a requisição de uma análise pelo Motor do Pegabot.

Reunimos aqui as diretrizes para ajudá-lo a descobrir onde você pode ser mais útil.

## Índice

0. [Tipos de contribuições que estamos procurando](#tipos-de-contribuições-que-procuramos)
0. [Regras básicas e expectativas](#regras-básicas-e-expectativas)
0. [Como contribuir](#como-contribuir)
0. [Configurando seu ambiente](#configurando-seu-ambiente)
0. [Comunidade](#comunidade)

## Tipos de contribuições que procuramos

"Listagem dos tipos de contribuições esperados"

Interessado em contribuir neste projeto? Leia!

## Regras básicas e expectativas

Antes de começarmos, aqui estão algumas coisas que esperamos de você (e que você deve esperar dos outros):

* Seja gentil e atencioso em suas conversas sobre este projeto. Todos nós viemos de diferentes origens e projetos, o que significa que provavelmente temos diferentes perspectivas sobre "como o código aberto é feito". Tente ouvir os outros em vez de convencê-los de que seu caminho está correto.
* Este projeto conta com um [Código de Conduta do Contribuidor](./CODE_OF_CONDUCT.md). Ao participar deste projeto, você concorda em cumprir seus termos.

## Como contribuir

Se você quiser contribuir, comece pesquisando em [issues](https://github.com/caminhodoprojeto/issues) e [pull requests](https://github.com/caminhodoprojeto/pulls) para ver se alguém levantou uma ideia ou pergunta semelhante.

Se você não vir sua ideia listada e achar que ela se encaixa nos objetivos deste guia, abra uma nova issue.

## Configurando seu ambiente

### Como instalar
  
Este código é executado com `python 3.9.4` e `pip 20.2.3`.
  
### 1. Instale o pacote virtualenv em seu python via pip
  
No terminal, basta executar:
  
`python -m pip install --user virtualenv`

### 2. Instalando o sqlite3
`$ pip instalar pysqlite3`
`$ pip instalar poesia`
  
### 3. Crie um ambiente virtual
  
No tipo de terminal, dentro da pasta do projeto digite:
  
`virtualenv .venv`

e você deverá ver um diretório `.env/` dentro da pasta do seu projeto ou com o nome que você escolheu no passo anterior.

Agora, ative o ambiente virtual:

`source .venv/bin/activate`
  
### 4. Crie seu arquivo `.env` localmente
  
no terminal, dentro da pasta do projeto apenas copie e renomeie o `example.env` para `.env`

`$ cp example.env .env`

preencha a string `.env` com suas credenciais de desenvolvedor do Twitter (veja as instruções abaixo)

### 5. Mantendo as dependências do projeto atualizadas usando `poetry`

#### 5.1 Instalando dependências do projeto de `pyproject.toml`

`instalação de poesia`

#### 5.2 Defina o poetry para trabalhar com seu `.venv/` local

`poetry config virtualenvs.create false --local`

#### 5.3 Verifique suas configurações do poetry:

`configuração de poesia --list`

O resultado deve ser algo como abaixo:
```console
cache-dir = "/Users/dc/Library/Caches/pypoetry"
experimental.new-installer = true
installer.parallel = true
virtualenvs.create = false
virtualenvs.in-project = true
virtualenvs.path = "{cache-dir}/virtualenvs"  # /Users/dc/Library/Caches/pypoetry/virtualenvs
```

### 6. Criando o banco de dados

#### 6.1 Crie um arquivo .db em `API/app/`

`$ cd API/app`
</br>
`$ touch mydatabase.db` Você pode criar manualmente

#### 6.2. Defina suas variáveis ​​no arquivo `.env`.
####Se você planeja usar outro sistema de banco de dados, visite Flask [https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/]

````
twitter_api_key=""
twitter_api_secret=""
twitter_access_token=""
twitter_access_token_secret=""
DATABASE_URL=sqlite:////mydatabase.db'
````

#### 6.3 Criando tabelas de banco de dados usando sqlalchemy

`flask db upgrade` para gerar arquivos de migração # se eles não existirem
</br>
`flask db migrate` para criar as próprias tabelas

#### 6.4 verificando se as tabelas foram criadas
`sqlite3 mydatabase.db`
#### 6.5 Uma vez no console sqlite3 digite o seguinte comando para verificar o esquema criado
`$ .schema`

Você deve ver algo assim:

``` 
sqlite> .schema
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
CREATE TABLE analises (
	id INTEGER NOT NULL, 
	handle VARCHAR(80) NOT NULL, 
	total VARCHAR(120), 
	network VARCHAR(120), 
	sentiment VARCHAR(120), 
	friends VARCHAR(120), 
	temporal VARCHAR(120), 
	twitter_id VARCHAR(120), 
	twitter_handle VARCHAR(120), 
	twitter_user_name VARCHAR(120), 
	twitter_is_protected BOOLEAN, 
	twitter_user_description VARCHAR(255), 
	twitter_followers_count INTEGER, 
	twitter_friends_count INTEGER, 
	twitter_location VARCHAR(120), 
	twitter_created_at TIMESTAMP, 
	twitter_is_verified BOOLEAN, 
	twitter_lang TIMESTAMP, 
	twitter_default_profile VARCHAR(255), 
	twitter_profile_image VARCHAR(255), 
	twitter_withheld_in_countries VARCHAR(255), 
	cache_times_served INTEGER, 
	cache_validity TIMESTAMP, pegabot_version VARCHAR(255), created_at DATETIME, updated_at DATETIME, 
	PRIMARY KEY (id), 
	CHECK (twitter_is_verified IN (0, 1))
);
CREATE TABLE feedbacks (
	id INTEGER NOT NULL, 
	analisis_id VARCHAR(80) NOT NULL, 
	feedback BOOLEAN NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE relatorios (
	id INTEGER NOT NULL, 
	report_name VARCHAR NOT NULL, 
	analise_id VARCHAR(80) NOT NULL, 
	PRIMARY KEY (id)
);
```

### 7. Executando o projeto para desenvolvimento

O script `init.sh` contém os comandos necessários para você executar o projeto.

No seu terminal
```console
./init.sh
```

### ou apenas use os seguintes comandos na raiz do projeto ``$ API/``

```console
$ poetry shell
$ export FLASK_APP=app/api.py
$ export FLASK_ENV=development
$ poetry install
$ poetry run flask run
```

## Comunidade

As discussões sobre o projeto ocorrem nas seções [Issues](https://github.com/caminhodoprojeto/issues) e [Pull Requests](https://github.com/caminhodoprojeto/pulls). Qualquer pessoa é bem-vinda para participar dessas conversas.

Sempre que possível, não leve essas conversas para canais privados, inclusive entrando em contato diretamente com os mantenedores. Manter a comunicação pública significa que todos podem se beneficiar e aprender com a conversa.

Esse arquivo foi elaborado com base [neste](https://github.com/github/opensource.guide/blob/main/CONTRIBUTING.md) repositório.
