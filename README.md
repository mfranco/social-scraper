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


5. Index facebook users by command line

    * Fill data.txt file with terms that want to search.
    * pyton manage.py index_facebook


6. Index twitter users by command line

    * Fill data.txt file with terms that want to search.
    * pyton manage.py index_twitter


7. Run Rest API:
        python manage.py runserver



User API
--------

A REST interface that serves client request for username the root of the  API will be:

    http://[hostname]/social-scraper/api/v1.0/


Get User list
-------------

A  GET call to get user list:

    curl  localhost:5000/social-scraper/api/v1.0/users/


Will return:
    
    {u'user_list': [{u'popularity_index': None, u'source': u'Facebook', u'username': u'100003958401468', u'description': u''}, {u'popularity_index': None, u'source': u'Facebook', u'username': u'100001491026412', u'description': u''}, {u'popularity_index': None, u'source': u'Facebook', u'username': u'100003038015381', u'description': u''}, {u'popularity_index': None, u'source': u'Facebook', u'username': u'100000732003283', u'description': u''}, {u'popularity_index': None, u'source': u'Facebook', u'username': u'100003822890655', u'description': u''}, {u'popularity_index': None, u'source': u'Facebook', u'username': u'100004671217557', u'description': u''}, {u'popularity_index': None, u'source': u'Facebook', u'username': u'100003620553914', u'description': u''}, {u'popularity_index': None, u'source': u'Facebook', u'username': u'100005912768970', u'description': u''}, {u'popularity_index': None, u'source': u'Facebook', u'username': u'100001897464570', u'description': u''}, {u'popularity_index': None, u'source': u'Facebook', u'username': u'550106197', u'description': u''}, {u'popularity_index': 157, u'source': u'Facebook', u'username': u'JhonSmithJs', u'description': u''}]}


Get Or Create User
------------------

A POST request will get or create an user or user that match with the search term:

    curl -X POST localhost:5000/social-scraper/api/v1.0/users/ -H "Content-Type: application/json" \
     -d '{"username": "JhonSmithJs"}'

Will return:

    {
      "user_list": [
        {
          "description": "", 
          "popularity_index": 157, 
          "source": "Twitter", 
          "username": "JhonSmithJs"
        }
      ]
    }

See also
---------
[Python httplib2](http://code.google.com/p/httplib2/)

[Flask Framework Website](http://flask.pocoo.org)


[Sqlalchemy Website](http://www.sqlalchemy.org/)

