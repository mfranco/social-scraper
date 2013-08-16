from scrapers.facebook import FacebookScraper
from scrapers.twitter import TwitterScraper
from test.base import ApiBaseTestCase
from users.models import User
from users.views import *

import json


class UserViewsTestCase(ApiBaseTestCase):
    def setUp(self):
        super(UserViewsTestCase, self).setUp()
        self.users_url = '{0}/users/'.format(UserAPIView.ENDPOINT)

    def create_users(self):
        term = 'Jhon Smith'
        scraper = FacebookScraper()
        scraper.search_profile_by_term(term)
        scraper = TwitterScraper()
        scraper.search_profile_by_term(term)

    def test_get_user_list(self):
        self.create_users()
        response = self.json_request(self.users_url, method='get')
        json_dict_response = json.loads(response.data)
        self.assertEquals(User.objects.filter_by().count(), len(json_dict_response['user_list']))

    def test_create_user(self):
        self.assertEquals(0, User.objects.filter_by().count())
        data = {'username': 'JhonSmithJs'}
        response = self.json_request(self.users_url, data=data)
        self.assertNotEquals(0, User.objects.filter_by().count())
