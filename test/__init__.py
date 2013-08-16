from test.models import *
from test.views import *
from test.facebook.test_facebook import FacebookTestCase
from test.twitter.test_twitter import TwitterTestCase

def init_test():
    import unittest
    #suite1 = unittest.TestLoader().loadTestsFromTestCase(UserModelTestCase)
    #suite2 = unittest.TestLoader().loadTestsFromTestCase(UserViewsTestCase)
    #alltests = unittest.TestSuite([suite1, suite2])
    suite1 = unittest.TestLoader().loadTestsFromTestCase(FacebookTestCase)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TwitterTestCase)
    alltests = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner(verbosity=2).run(alltests)
