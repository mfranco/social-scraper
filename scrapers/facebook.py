from common.scraper import BaseScraper
from users.models import User

from bs4 import BeautifulSoup

import json
import re
import sys


class FacebookScraper(BaseScraper):
    def __init__(self, *args, **kwargs):
        super(FacebookScraper, self).__init__(self, *args, **kwargs)
        self.base_url = 'https://www.facebook.com/'
        if 'test' in sys.argv:
            from test.facebook.mock_api import FacebookMockRequest
            self.h = FacebookMockRequest()

    def get_profile_by_url(self, url):
        resp, content = self.request(url, 'GET')
        return content

    def search_profile_by_term(self, term):
        """perform a request to facebook public profile searcher by term, parse html and store
           users information
        """
        kwargs = {'params': {'q': term},
                 'path': 'search.php?'}
        resp, content = self.get(**kwargs)
        page =  BeautifulSoup(content)
        search_results = page.find(id='pagelet_search_results')
        json_data_regular = re.compile(r'{ search_logged_ajax\((?P<json_content>.*)\);.*tabindex')
        name_regular = re.compile(r'<h2 itemprop="name">(?P<name>.*)</h2>')

        for div in search_results.find_all('div', class_='detailedsearch_result'):
            try:
                jdata = json.loads(json_data_regular.search(str(div)).group('json_content'))
                html_profile = self.get_profile_by_url(jdata['cururl'])
                name = name_regular.search(html_profile).group('name')
                user = User(name=name, username=jdata['id'],
                            json_context=jdata, source=User.SOURCE_ENUM.FACEBOOK)
                user.add()
            except Exception as error:
                print error
                pass

def index_profiles_by_term(term_list):
    for term in term_list:
        scrapper = FacebookScraper()
        scrapper.search_profile_by_term(term)
