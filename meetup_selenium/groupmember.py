"""
Module to represent meetup group members
"""
class GroupMember():
    """Class to represent a meetup group member """

    def __init__(self, *, name=None, url=None, user_id=None, joined=None):
        self.name = name
        self.url = url
        self.user_id = user_id
        self.joined = joined

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __repr__(self):
        return str(self.__class__) + ": " + str(self.__dict__)
