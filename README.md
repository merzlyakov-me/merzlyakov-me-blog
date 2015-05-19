# merzlyakov-me-blog
Blog @ merzlyakov.me sources

# Server-side setup
## Database setup
### Installation
* sudo aptitude install postgresql postgresql-contrib
* sudo aptitude install postgresql-9.3-postgis-2.1
* sudo aptitude install libpq-dev python-dev
### Setup
* sudo -u postgres psql postgres
* \password postgres
* sudo su - postgres
* createdb merzlyakov
* createuser -P -s -e merzlyakov
* psql> GRANT ALL PRIVILEGES ON DATABASE merzlyakov TO merzlyakov;
### Install python libraries
* pip install psycopg2
## Setup django to connect to db
### apply changes
* ./manage.py migrate
### Create superuser
* ./manage.py createsuperuser

## Install Grappelli


# TODO:
* Add statistics
* Add visitors collecting
