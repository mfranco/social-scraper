from scrapers.facebook import FacebookScraper
from test.base import ApiBaseTestCase
from users.models import User

class FacebookTestCase(ApiBaseTestCase):
    def test_search_profiles_by_term(self):
        self.assertEquals(0, User.objects.filter_by().count())
        term = 'Jhon Smith'
        scraper = FacebookScraper()
        scraper.search_profile_by_term(term)
        self.assertNotEquals(0, User.objects.filter_by().count())
