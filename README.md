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
