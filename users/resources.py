from common.resources import BaseResource
from scrapers.facebook import FacebookScraper
from scrapers.twitter import TwitterScraper
from users.models import User

class UserResource(BaseResource):
    __model__ = User

    def __init__(self, data, **kwargs):
        super(UserResource, self).__init__(data, **kwargs)
        self._is_valid = True

    def get_or_create(self):
        user_list = self.filter_by(username=self._dict_data['username'])
        if not user_list:
            term = self._dict_data['username']
            scraper = FacebookScraper()
            scraper.search_profile_by_term(term)
            scraper = TwitterScraper()
            scraper.search_profile_by_term(term)
        user_list = self.filter_by(username=self._dict_data['username'])
        return user_list

