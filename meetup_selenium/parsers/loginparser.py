"""Module to support parsing of the meetup login page """
import sys

from .parseutil import *
from .exception import ParseError
from ..util import yes_or_no

class LoginParser():
    """Class to interact with the login page """

    def __init__(self, driver):
        self.driver = driver

    def load_initial(self, url):
        """Load the login page """
        self.driver.get(url)

        xpath_page_loaded = '//form[@class="loginForm"]'

        wait_element(self.driver, xpath_page_loaded)

        if not get_element(self.driver, xpath_page_loaded):
            raise ParseError(xpath_page_loaded, "Unable to load login page")

    def login(self, username, password):
        """Login into meetup """
        print_pretty("Going to login into meetup with user '" + username + "'")

        in_email = self.get_in_mail()
        in_password = self.get_in_password()

        in_email.clear()
        in_email.send_keys(username)
        in_password.clear()
        in_password.send_keys(password)
        click_element(self.driver, '//input[@id="loginFormSubmit"]')

        if self.need_captcha_solving():
            print_pretty("Your account", username, "needs a security check!")
            if not yes_or_no("Did you solve the captcha"):
                sys.exit(0)

        self.wait_logged_in()

        if self.logged_in():
            print_pretty("Login into linkedin: SUCCESS")
            return True
        else:
            print_pretty("Login into linkedin: FAILED")
            return False

    def wait_logged_in(self):
        """Wait for your account to be logged in """
        wait_element(self.driver, '//input[@id="mainKeywords"]')

    def logged_in(self):
        """Verify if you are logged in """
        return has_element(self.driver, '//input[@id="mainKeywords"]')

    def get_in_mail(self):
        """Get the email input element on this page """
        return get_element(self.driver, '//input[@id="email"]')

    def get_in_password(self):
        """Get the password input element on this page """
        return get_element(self.driver, '//input[@id="password"]')

    def need_captcha_solving(self):
        """Verify if a captcha is needed """
        return has_element(self.driver, '//div[@class="g-recaptcha"]')
 