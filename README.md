# Repository for the Pegabot API

## How to install
  
This code run with `python 3.9.4` and `pip 20.2.3`. The packages are listed at the `requirements.txt` file.  
   
  
## install the virtualenv package on your python via pip  
  
at the terminal just run:  
  
`python -m pip install --user virtualenv`  
  
## create a virtual environment   
  
At the terminal type, inside the project folder type:  
  
`virtualenv .venv`   

and you should see a `.env/` dir inside your project folder or with the given name you choose at the step before.  

Now, activate the virtual environment:

`source .venv/bin/activate` 
  
## step 1: give permission to `init.sh` file to run  
  
```console
chmod +x init.sh
```
  
## step 2: create your .env file locally  
  
on terminal, inside the project folder just copy and rename the `.env-example` to `.env`  
  
`$ cp .env-example .env`

fill the `.env` file with the proper info

## step 3: Keeping the project dependencies up-to-date using `poetry`

### first install poetry on your local python (not your virtual env)  

`pip install poetry`

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

### Example: adding `flask` to the project

`poetry add flask`

## step 4: creating the database

Simply run:

`flask db upgrade`
`flask db migrate`

## step 5: running the project for delopment

The script `init.sh` contains the commands necessary for your to install your `requirements.txt`file and run the project.

On your terminal 
```console
./init.sh
```
