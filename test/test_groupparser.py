"""Package to test GroupParser """
import os
import unittest
import selenium

from meetup_selenium import driver
from meetup_selenium.parsers import groupparser

class GroupParserTest(unittest.TestCase):
    """Class to test GroupParser """
    mydriver = None

    @classmethod
    def setUpClass(cls):
        group_html = "file://" + os.path.abspath("test/html_files/group.html")
        cls.mydriver = driver.init_webdriver(driver_name="chrome", headless=True)
        cls.mydriver.get(group_html)

    @classmethod
    def tearDownClass(cls):
        cls.mydriver.close()

    def setUp(self):
        self.group_parser = groupparser.GroupParser(self.__class__.mydriver)

    def test_get_name(self):
        '''Test function '''
        result = self.group_parser.get_name()
        self.assertIsNotNone(result)
        self.assertTrue(result)
        self.assertEqual(result, "Ansible London")

    def test_get_location(self):
        '''Test function '''
        result = self.group_parser.get_location()
        self.assertIsNotNone(result)
        self.assertTrue(result)
        self.assertEqual(result, "London, United Kingdom")

    def test_get_joined(self):
        '''Test function '''
        result = self.group_parser.get_joined()
        self.assertIsNotNone(result)
        self.assertTrue(result)

    def test_get_member_count(self):
        '''Test function '''
        result = self.group_parser.get_member_count()
        self.assertIsNotNone(result)
        self.assertEqual(result, 2255)

    def test_get_description(self):
        '''Test function '''
        result = self.group_parser.get_description()
        self.assertIsNotNone(result)
        self.assertTrue(result.startswith("We are a group of Systems Engineers and DevOps folks"))

    def test_get_menu_about(self):
        '''Test function '''
        result = self.group_parser.get_menu_about()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

    def test_get_menu_events(self):
        '''Test function '''
        result = self.group_parser.get_menu_events()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

    def test_get_menu_members(self):
        '''Test function '''
        result = self.group_parser.get_menu_members()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

    def test_get_menu_photos(self):
        '''Test function '''
        result = self.group_parser.get_menu_photos()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

    def test_get_menu_discussions(self):
        '''Test function '''
        result = self.group_parser.get_menu_discussions()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

if __name__ == '__main__':
    unittest.main()
