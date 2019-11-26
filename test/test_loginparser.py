"""Package to test LoginParser """
import os
import unittest
import selenium

from meetup_selenium import driver
from meetup_selenium.parsers import loginparser

class LoginParserTest(unittest.TestCase):
    """Class to test LoginParser """
    mydriver = None

    @classmethod
    def setUpClass(cls):
        cls.mydriver = driver.init_webdriver(driver_name="chrome", headless=True)

    @classmethod
    def tearDownClass(cls):
        cls.mydriver.close()

    def setUp(self):
        login_test_page = "file://" + os.path.abspath("test/html_files/login.html")
        self.login_parser = loginparser.LoginParser(self.__class__.mydriver)
        self.login_parser.load_initial(login_test_page)

    def test_get_in_mail(self):
        '''Test function '''
        result = self.login_parser.get_in_mail()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

    def test_get_in_password(self):
        '''Test function '''
        result = self.login_parser.get_in_password()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, selenium.webdriver.remote.webelement.WebElement)

    def test_need_captcha_solving(self):
        '''Test function '''
        result = self.login_parser.need_captcha_solving()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
