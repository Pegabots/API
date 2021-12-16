# Repository for the Pegabot API

## How to install
  
This code run with `python 3.9.4` and `pip 20.2.3`. The packages are listed at the `requirements.txt` file.   
  
## install the virtualenv package on your python via pip  
  
at the terminal just run:  
  
`python -m pip install --user virtualenv`

# installing sqlite3 
`$ pip install pysqlite3`
`$ pip install poetry`
  
## create a virtual environment   
  
At the terminal type, inside the project folder type:  
  
`virtualenv .venv`   

and you should see a `.env/` dir inside your project folder or with the given name you choose at the step before.  

Now, activate the virtual environment:

`source .venv/bin/activate`
  
## create your `.env` file locally  
  
on terminal, inside the project folder just copy and rename the `.env-example` to `.env`  
  
`$ cp .env-example .env`

fill the `.env` string with your Twitter developer credentials (See instructions bellow)

## step 3: Keeping the project dependencies up-to-date using `poetry`

### Installing project dependencies from `pyproject.toml`

`poetry install`

### Set poetry to work with your local `.venv/` 

`poetry config virtualenvs.create false --local`

### Verify your poetry settings:

`poetry config --list`

The result should be something as bellow:
```console
cache-dir = "/Users/dc/Library/Caches/pypoetry"
experimental.new-installer = true
installer.parallel = true
virtualenvs.create = false
virtualenvs.in-project = true
virtualenvs.path = "{cache-dir}/virtualenvs"  # /Users/dc/Library/Caches/pypoetry/virtualenvs
```

## step 4: creating the database

#### create a .db file at the `pegabot-api/app/`

`$ cd pegabot-api/app`
</br>
`$ touch mydatabase.db` You can create manually

## step 4: set your variables at the `.env` file. 
####If you plan using other database system, you should visit Flask [https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/]

````
twitter_api_key=""
twitter_api_secret=""
twitter_access_token=""
twitter_access_token_secret=""
DATABASE_URL= sqlite:////mydatabase.db'
````

### creating database tables using sqlalchemy

`flask db upgrade` in order to generate migrations files # if they dont exists
</br>
`flask db migrate` in order to create the tables itself

### verifying if the tables were created
`sqlite3 mydatabase.db`
### once on sqlite3 console type the following command to check the created schema
`$ .schema`

You should see something like this:

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

## step 5: running the project for delopment

The script `init.sh` contains the commands necessary for your to install your `requirements.txt`file and run the project.

On your terminal 
```console
./init.sh
```

### or just use the following commands at the root of the project ``$ pegabot-api/``

```console
$ poetry shell
$ export FLASK_APP=app/api.py
$ export FLASK_ENV=development
$ poetry install
$ poetry run flask run
```
