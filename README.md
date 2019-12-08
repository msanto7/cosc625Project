# COSC 625 - Python Application

## Live site 
https://cosc625-group4.herokuapp.com/

## Group 4


## Project Description 
 

## Database 
--> PostgreSQL
--> ORM -- Psycopg2


## commands used

"pipenv shell --three" --> to setup virtual environment 
"pipenv install flask"  --> adds flask dependency
"pipenv install psycopg2-binary" --> 
"sudo apt-get install postgresql libpq-dev postgresql-client postgresql-client-common" --> to setup the postgreSQL env  
"pip install psychopg2" --> fixed error for ORM
"pipenv install flask-sqlalchemy --> used to map data objects
"pipenv install gunicorn" --> used to deploy to heroku 
"snap install --classic heroku" --> used for heroku deployment 

Heroku Deployment Steps 
--> heroku login
--> heroku create cosc625_group4
--> heroku addons:create heroku-postgresql:hobby-dev --app cosc625-group4
--> heroku config --app cosc625-group4
## set repo remote for our heroku project 

--> heroku git:remote -a cosc625-group4

# push code to heroku project 
--> git push heroku master



