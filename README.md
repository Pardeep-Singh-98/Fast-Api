# Fast Api jwt Token Professional file structure using Agile Approach

# Follow the steps : 

##  Step : 1

1. create virtual envoirment using command :>  python -m venv venv

## Step : 2

2. Activate Window : venv\Scripts\activate

## Step : 3

3. Install Packages : pip install fastapi uvicorn sqlalchemy python-jose passlib[bcrypt] python-multipart email-validator pymysql

# what these packages about
Package                                 Purpose

fastapi                                 Api framework
uvicor                                  Run server
sqlalchemy                              ORM
python-jose                             JWT
passlib                                 Password hashing
python-multipart                        Handle Form Data and file Uploads
email-validator                         Email Formatted or Valid


## Step : 4

4. we are goint to hit this command in our terminal : pip freeze > requirements.txt

  purpose of this command it will avoid all the global packages. because when we push this project to github we will not upload our virtual envoirment folder , becuase it has so many files and folder that we didn't use yet , so this command copy all the packages in requirement.txt file so another user who will download the repo can use this 'pip install -r requirements.txt' command to install only limited package rather than all global packages.

## Step : 5

5. **Make .gitignore file to avoid venv folder or __pycache__ folders

