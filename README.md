# CCDB

A collections and contaminants database.

## Development Setup

    $ pyvenv venv
    $ source venv/bin/activate
    $ pip install -r requirements/local.txt
    $ createdb ccdbdjango
    $ python manage.py migrate
    $ python manage.py runserver

## Basic Commands

### Setting Up Your Users

To create a **normal user account**, just go to Sign Up and fill out the form.
Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your
console to see a simulated email verification message. Copy the link into your
browser. Now the user's email should be verified and ready to go.

To create a **superuser account**, use this command::

    $ python manage.py createsuperuser


## Deploying to Heroku

    heroku create --buildpack https://github.com/heroku/heroku-buildpack-python

    heroku addons:create heroku-postgresql:hobby-dev
    heroku pg:backups schedule --at '02:00 America/Los_Angeles' DATABASE_URL
    heroku pg:promote DATABASE_URL

    heroku config:set DJANGO_ADMIN_URL=`openssl rand -base64 32`
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 64`
    heroku config:set DJANGO_SETTINGS_MODULE='config.settings.production'
    heroku config:set DJANGO_ALLOWED_HOSTS='.herokuapp.com'

    heroku config:set DJANGO_AWS_ACCESS_KEY_ID=YOUR_AWS_ID_HERE
    heroku config:set DJANGO_AWS_SECRET_ACCESS_KEY=YOUR_AWS_SECRET_ACCESS_KEY_HERE
    heroku config:set DJANGO_AWS_STORAGE_BUCKET_NAME=YOUR_AWS_S3_BUCKET_NAME_HERE

    heroku config:set DJANGO_MAILGUN_SERVER_NAME=YOUR_MALGUN_SERVER
    heroku config:set DJANGO_MAILGUN_API_KEY=YOUR_MAILGUN_API_KEY

    heroku config:set PYTHONHASHSEED=random
    heroku config:set DJANGO_ADMIN_URL=\^somelocation/

    git push heroku master
    heroku run python manage.py migrate
    heroku run python manage.py check --deploy
    heroku run python manage.py createsuperuser
    heroku open
