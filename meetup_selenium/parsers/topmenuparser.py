"""
Module to support parsing of top menu
"""
from .parseutil import *

class TopMenuParser():
    """
    Class to interact with the top menu
    """
    def __init__(self, driver):
        """ Constructor for this class """
        self.driver = driver

    def logout(self):
        """
        Logout of meetup
        """
        print_pretty("Going to logout from meetup")

        menu_settings = self.get_menu_settings_dropdown()
        menu_settings.click()
        menu_logout = self.get_menu_logout()
        menu_logout.click()

        wait_page_loaded(self.driver, "https://www.meetup.com/apps/")
        self.wait_logged_out()

        if self.logged_out():
            print_pretty("Logged out from meetup: SUCCESS")
            return True
        else:
            print_pretty("Logged out from meetup: FAILED")
            return False

    def wait_logged_out(self):
        """
        Wait for your account to be logged out
        """
        return wait_element(self.driver, '//span[text()="Log in"]')

    def logged_out(self):
        """
        Verify if you are logged out
        """
        return has_element(self.driver, '//span[text()="Log in"]')

    def get_menu_settings_dropdown(self):
        """
        Get the settings menu on this page
        """
        return get_element(self.driver, '//span[@id="headerAvatar"]')

    def get_menu_logout(self):
        """
        Get the logout menu on this page
        """
        return get_element(self.driver, '//a[text()="Log out"]')

    def get_menu_explore(self):
        """
        Get the explore menu on this page
        """
        return get_element(self.driver, '//span[text()="Explore"]')

    def get_menu_messages(self):
        """
        Get the messages menu on this page
        """
        return get_element(self.driver, '//span[contains(text(), "Messages")]')

    def get_menu_notifications(self):
        """
        Get the notifications menu on this page
        """
        return get_element(self.driver, '//span[text()="Notifications"]')
