"""Module to represent meetup searches """
from .parsers.searchparser import SearchParser
from .searchradius import SearchRadius

from .util import print_pretty

class GroupSearcher():
    """Class to search for meetup groups adn events """

    def __init__(self, driver):
        self.driver = driver

    def search_group(self, keyword, radius, location):
        """Function to search for meetup groups"""

        if not radius in [SearchRadius.TWO_MILES, SearchRadius.FIVE_MILES, SearchRadius.TEN_MILES,
                          SearchRadius.TWENTYFIVE_MILES, SearchRadius.FIFTHY_MILES, SearchRadius.HUNDRED_MILES,
                          SearchRadius.ANY_DISTANCE]:
            print_pretty("Invalid value for search radius,lease use the SearchRadius class.")
            return []

        search_parser = SearchParser(self.driver)
        search_parser.load_initial("https://www.meetup.com/find")
        return search_parser.search_group(keyword, radius, location)
