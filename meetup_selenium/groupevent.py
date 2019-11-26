"""
Module to represent meetup group events
"""
class GroupEvent():
    """Class to represent a meetup group event """

    def __init__(self, *, name=None, url=None, date=None, location=None, description=None, cnt_attendees=None):
        self.name = name
        self.url = url
        self.date = date
        self.location = location
        self.description = description
        self.cnt_attendees = cnt_attendees

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
