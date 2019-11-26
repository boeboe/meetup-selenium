"""
Module to represent meetup members
"""
from .parsers.memberparser import MemberParser

class Member():
    """Class to represent a meetup member """

    def __init__(self, *, driver, url):
        self.url = url
        self.parse(driver)

    def parse(self, driver):
        """Function to parse a meetup member """
        parser = MemberParser(driver)
        parser.load_initial(self.url)

        self.name = parser.get_name()
        self.location = parser.get_location()
        self.joined = parser.get_date_joined()
        self.bio = parser.get_bio()
        self.facebook = parser.get_facebook()
        self.twitter = parser.get_twitter()
        self.flickr = parser.get_flickr()
        self.tumblr = parser.get_tumblr()
        self.interests = parser.get_interests()
        self.groups = parser.get_groups()

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
