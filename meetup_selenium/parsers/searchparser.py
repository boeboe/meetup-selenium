"""Module to support parsing of meetup searches """
from selenium.webdriver.common.keys import Keys

from .parseutil import *
from .exception import ParseError


class SearchParser():
    """Class to interact with the meetup search page """

    def __init__(self, driver):
        self.driver = driver

    def load_initial(self, url):
        """Load the search page """
        self.driver.get(url)

        xpath_page_loaded = '//input[@id="mainKeywords"]'
        wait_element(self.driver, xpath_page_loaded)

        if not get_element(self.driver, xpath_page_loaded):
            raise ParseError(xpath_page_loaded, "Unable to load search page")

    def search_group(self, keyword, radius, location):
        """Search a group by keyword """

        self.set_search(keyword)
        self.set_distance(radius)
        self.set_location(location)

        click_element(self.driver, '//i[@class="icon-search"]')
        return self.get_groups()


    def set_search(self, keyword):
        """Set the keyword in the search field on this page """
        in_search = get_element(self.driver, '//input[@id="mainKeywords"]')
        in_search.clear()
        in_search.send_keys(keyword)

    def set_distance(self, radius):
        """Set the distance using radius dropdown on this page """
        click_element(self.driver, '(//form[@id="searchForm"]//a[@class="dropdown-toggle"])[1]')
        click_element(self.driver, '//a[@data-copy="{}"]'.format(radius))

    def set_location(self, location):
        """Set the location using location dropdown on this page """
        click_element(self.driver, '(//form[@id="searchForm"]//a[@class="dropdown-toggle"])[2]')

        in_location = get_element(self.driver, '//input[@id="locationSearch"]')
        in_location.clear()
        in_location.send_keys(location)
        in_location.send_keys(Keys.RETURN)

    def get_groups(self):
        """Get the groups matching the search """
        load_infinite_page(self.driver, '//a[@itemprop="url"]', '//span[text()="Show more"]')
        return get_attributes(self.driver, '//a[@itemprop="url"]', "href")
