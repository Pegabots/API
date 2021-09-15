# before you go, take a moment to use the best practices for this repository

This code was run with `python 3.9.4`. The packages are listed at the `requirements.txt` file.

I strongly recommend using `pyenv` to maintain multiple versions of python installed locally. 

## install the virtualenv package on your python via pip

at the terminal just run:

`python -m pip install --user virtualenv`

## create your virtual env. 

Once you have your virtual env created, the packages you once install will not affect your local python packages. Which will avoid conflits. A good practice is to have a virtualenv per project.

The community convention is to use the name `venv` for the environment you are about to create. 

to create your virtualven just type the following command at your terminal:

`virtualenv venv` 

and you should see a `/env/` directory inside your project folder or with the given name you choose at the step before.


## step 1: go to your local repository and type on your terminal:

Warning: Now you should active your `virtualenv`. Keep in mind you need to activate everytime you begin to work with the project. Otherwise, the packages you once install on your virtualenv won't be available to your local python.

#### Linux/Macos

Active your virtualenv using the command source, if you are using linux-like bash. If you are using Windows the command can be diffrent. 

`source venv/bin/activate`

If your terminal looks like the above, you are good.

`(venv) dc@blckjzz pegabot-twitter-api % `

#### For Windows Users

`\env\Scripts\activate.bat`


## step 2: once your virtualenv

Now you should have your virtualenv setup. It's time to install the required packages for running this project.

On terminal at the project folder type:

`pip install -r requirements.txt `


## step 3: create your .env file locally

on terminal, inside the project folder just copy and rename the `.env-example` to `.env`

`$ cp .env.example .env`

### Update your virtualenv packages
#### everytime you need to update your requirements.txt file, you should generate an updated version of your `virtualenv` to a requirements.txt file

Go to your terminal and type

`pip freeze > requirements.txt`

After that, you should commit only your `requirements.txt` file instead your virtualenv `/venv` directory (which is ignored by default on this project on .gitignore file)

## Step 4: Using the virtualenv with Jupyter notebooks

For this you should need a package `ipykernel`, which will allow you to link your local venv with your Jupyter notebook. You should do this in order to use the venv and its packages on your notebook. 

At your terminal type:

`source venv/bin/activate` if not activated

`pip install ipykernel` if you have not installed previously. I added this package to the `requirements.txt` file so you should be fine.

`python -m ipykernel install --user --name=${PWD##*/}`

You should see a message like the above:

`Installed kernelspec pegabot-twitter-api in /Users/dc/Library/Jupyter/kernels/pegabot-twitter-api`

Once you hit the command above, you should restart your Jupyter server to load the new Kernel. You may stop the server or just restart the kernel.

Now you have a new kernel for your jupyter notebooks and should indicate which kernel to use in your project.

To do this go to your project, open any file `.ipynb`. At the upper menu bar find `Kernel > Change Kernel > ` and select your new kernel. If you used the same command as above, the kernel should be named as the same as the project, which is `pegabot-twitter-api` in my case.