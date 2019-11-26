"""Package to test TopMenuParser """
import os
import unittest
import selenium

from meetup_selenium import driver
from meetup_selenium.parsers import topmenuparser

class TopMenuParserTest(unittest.TestCase):
    """Class to test TopMenuParser """
    mydriver = None

    @classmethod
    def setUpClass(cls):
        top_menu_html = "file://" + os.path.abspath("test/html_files/top_menu.html")
        cls.mydriver = driver.init_webdriver(driver_name="chrome", headless=True)
        cls.mydriver.get(top_menu_html)

    @classmethod
    def tearDownClass(cls):
        cls.mydriver.close()

    def setUp(self):
        self.topmenu_parser = topmenuparser.TopMenuParser(self.__class__.mydriver)

    def test_get_menu_settings_dropdown(self):
        '''Test function '''
        result = self.topmenu_parser.get_menu_settings_dropdown()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

    def test_get_menu_logout(self):
        '''Test function '''
        result = self.topmenu_parser.get_menu_logout()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

    def test_get_menu_explore(self):
        '''Test function '''
        result = self.topmenu_parser.get_menu_explore()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

    def test_get_menu_messages(self):
        '''Test function '''
        result = self.topmenu_parser.get_menu_messages()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

    def test_get_menu_notifications(self):
        '''Test function '''
        result = self.topmenu_parser.get_menu_notifications()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

if __name__ == '__main__':
    unittest.main()
