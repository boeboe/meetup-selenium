"""Package to test MemberParser """
import os
import unittest
import selenium

from meetup_selenium import driver
from meetup_selenium.parsers import memberparser

class MemberParserTest(unittest.TestCase):
    """Class to test MemberParser """
    mydriver = None

    @classmethod
    def setUpClass(cls):
        member_html = "file://" + os.path.abspath("test/html_files/member_details.html")
        cls.mydriver = driver.init_webdriver(driver_name="chrome", headless=True)
        cls.mydriver.get(member_html)

    @classmethod
    def tearDownClass(cls):
        cls.mydriver.close()

    def setUp(self):
        self.member_parser = memberparser.MemberParser(self.__class__.mydriver)

    def test_get_name(self):
        '''Test function '''
        result = self.member_parser.get_name()
        self.assertIsNotNone(result)
        self.assertTrue(result)
        self.assertEqual(result, "Van Bos Bart")

    def test_get_location(self):
        '''Test function '''
        result = self.member_parser.get_location()
        self.assertIsNotNone(result)
        self.assertTrue(result)
        self.assertEqual(result, "Duffel")

    def test_get_date_joined(self):
        '''Test function '''
        result = self.member_parser.get_date_joined()
        self.assertIsNotNone(result)
        self.assertEqual(result, "January 6, 2014")

    def test_get_bio(self):
        '''Test function '''
        result = self.member_parser.get_bio()
        self.assertIsNotNone(result)
        self.assertTrue("engineer with a no nonsense approach" in result)

    def test_get_facebook(self):
        '''Test function '''
        result = self.member_parser.get_facebook()
        self.assertIsNotNone(result)
        self.assertTrue("http" in result)
        self.assertTrue("facebook" in result)

    def test_get_twitter(self):
        '''Test function '''
        result = self.member_parser.get_twitter()
        self.assertIsNotNone(result)
        self.assertTrue("http" in result)
        self.assertTrue("twitter" in result)

    def test_get_flickr(self):
        '''Test function '''
        result = self.member_parser.get_flickr()
        self.assertIsNotNone(result)
        self.assertTrue("http" in result)
        self.assertTrue("flickr" in result)

    def test_get_tumblr(self):
        '''Test function '''
        result = self.member_parser.get_tumblr()
        self.assertIsNotNone(result)
        self.assertTrue("http" in result)
        self.assertTrue("tumblr" in result)

    def test_get_interests(self):
        '''Test function '''
        result = self.member_parser.get_interests()
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 17)

    def test_get_groups(self):
        '''Test function '''
        result = self.member_parser.get_groups()
        self.assertIsNotNone(result)
        self.assertEqual(len(result), 39)
        self.assertTrue("https://www.meetup.com/" in result[0])


if __name__ == '__main__':
    unittest.main()
