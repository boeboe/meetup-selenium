"""Module to represent meetup groups """
from .parsers.groupparser import GroupParser

class Group():
    """Class to represent a meetup group """

    def __init__(self, *, driver, url):
        self.url = url

        self.name = None
        self.location = None
        self.joined = None
        self.member_count = None
        self.description = None

        self.parse(driver)

    def parse(self, driver):
        """Function to parse a meetup group """
        self.parser = GroupParser(driver)
        self.parser.load_initial(self.url)

        self.name = self.parser.get_name()
        self.location = self.parser.get_location()
        self.joined = self.parser.get_joined()
        self.member_count = self.parser.get_member_count()
        self.description = self.parser.get_description()

    def join(self):
        """Function to join a meetup group """
        self.parser.join()
        self.joined = self.parser.get_joined()

    def get_members(self):
        """Function to parse the members of a meetup group """
        return self.parser.get_members()

    def get_upcoming_events(self):
        """Function to parse the upcoming events a meetup group """
        return self.parser.get_upcoming_events()

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
