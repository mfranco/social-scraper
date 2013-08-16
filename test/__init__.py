from test.views import UserViewsTestCase
from test.facebook.test_facebook import FacebookTestCase
from test.twitter.test_twitter import TwitterTestCase

def init_test():
    import unittest
    suite1 = unittest.TestLoader().loadTestsFromTestCase(FacebookTestCase)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TwitterTestCase)
    suite3 = unittest.TestLoader().loadTestsFromTestCase(UserViewsTestCase)
    alltests = unittest.TestSuite([suite1, suite2, suite3])
    unittest.TextTestRunner(verbosity=2).run(alltests)
