Social Scraper
=================

A simple Facebook and Twitter Scraper that search information using public interfaces (without authentication)
on Facebook and Twitter. Retrieve Basic user information that later can be checked using an User RESTFUL API built using Flask Framework (http://flask.pocoo.org/) and Sqlalchemy
(http://www.sqlalchemy.org/)

Requirements
------------
Python 2.7.x


Installation
-------------

1. Create a virtual with:

        mkvirtualenv flaskapi
        workon flaskapi


2. Install requirements file:

        pip install -r requirements.txt


3. Run unit test suite:

        python manage.py test


4. Create database:

        python manage.py syncdb


5. Run app:

        python manage.py runserver






See also
---------
[Python httplib2](http://code.google.com/p/httplib2/)

[Flask Framework Website](http://flask.pocoo.org)


[Sqlalchemy Website](http://www.sqlalchemy.org/)

