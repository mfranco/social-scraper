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
        for div in search_results.find_all('div', class_='stream-item-header'):
            username = regular_username.search(str(div)).group('username')
            for t in term.split(' '):
                if t.lower() in username.lower():
                    self.get_profile()
                    break
        return 0

        json_data_regular = re.compile(r'{ search_logged_ajax\((?P<json_content>.*)\);.*tabindex')
        name_regular = re.compile(r'<h2 itemprop="name">(?P<name>.*)</h2>')

        for div in search_results.find_all('div', class_='detailedsearch_result'):
            try:
                jdata = json.loads(json_data_regular.search(str(div)).group('json_content'))
                """
                for item, value in jdata.items():
                    print '{0}: {1} \n'.format(item, value)
                """
                html_profile = self.get_profile_by_url(jdata['cururl'])
                name = name_regular.search(html_profile).group('name')
                user = User(name=name, username=jdata['id'], json_context=jdata)
                user.add()
            except Exception as error:
                print error
                pass

def index_profiles_by_term(term_list):
    for term in term_list:
        scrapper = TwitterScraper()
        scrapper.search_profile_by_term(term)
