"""Module to represent meetup accounts """
from .driver import init_webdriver
from .parsers.loginparser import LoginParser
from .parsers.topmenuparser import TopMenuParser

class Account():
    """Class to login and logout to a meetup account """

    def __init__(self, email, password, driver_name, headless=True):
        self.email = email
        self.password = password
        self.driver = init_webdriver(driver_name, headless)

    def login(self):
        """Function to login in meetup"""

        login_parser = LoginParser(self.driver)
        login_parser.load_initial("https://secure.meetup.com/login")
        login_parser.login(self.email, self.password)

        return self.driver

    def logout(self):
        """Function to logout from meetup"""

        logout_parser = TopMenuParser(self.driver)
        logout_parser.logout()
        return self.driver
