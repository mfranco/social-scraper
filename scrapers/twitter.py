from common.scraper import BaseScraper
from users.models import User

from bs4 import BeautifulSoup

import json
import re
import sys


class TwitterScraper(BaseScraper):
    def __init__(self, *args, **kwargs):
        super(TwitterScraper, self).__init__(self, *args, **kwargs)
        self.base_url = 'https://www.twitter.com/'
        self.user_agent = ''
        if 'test' in sys.argv:
            from test.twitter.mock_api import TwitterMockRequest
            self.h = TwitterMockRequest()

    def get_profile(self, username):
        kwargs = {'path': username}
        resp, content = self.get(**kwargs)
        return content

    def search_profile_by_term(self, term):
        """perform a request to twitter public profile searcher by term, parse html and store
           users information
        """
        kwargs = {'params': {'q': term},
                 'path': 'search?'}
        resp, content = self.get(**kwargs)
        page =  BeautifulSoup(content)
        search_results = page.find(id='stream-items-id')
        regular_username = re.compile(r'data-user-id=".*" href="/(?P<username>.*)"')

        def check_username(username):
            """Twitter search return users and twits with the term so we need to make sure that
               the username match with the search term before perform the insertion, if the seacrh
               term is compounded by most than one word we split the string a try to find a partial match
               by every word
            """
            for t in term.split(' '):
                if t.lower() in username.lower():
                    return True
            return False

        json_regular = re.compile(r"value='(?P<json_content>.*)'>")
        for div in search_results.find_all('div', class_='stream-item-header'):
            username = regular_username.search(str(div)).group('username')
            if check_username(username):
                try:
                    profile_page = BeautifulSoup(self.get_profile(username))
                    input_hidden_data =  profile_page.find(id='init-data')
                    jdata = json.loads(json_regular.search(str(input_hidden_data)).group('json_content'))
                    name = jdata['profile_user']['name']
                    popularity_index = jdata['profile_user']['followers_count']
                    user = User(username=username, name=name, json_context=jdata,
                                source=User.SOURCE_ENUM.TWITTER, popularity_index=popularity_index)
                    user.add()
                except Exception as error:
                    pass

def index_profiles_by_term(term_list):
    for term in term_list:
        scrapper = TwitterScraper()
        scrapper.search_profile_by_term(term)
