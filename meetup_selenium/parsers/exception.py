"""Module to represent parse errors """
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class ParseError(Error):
    """Exception raised for errors in the parsing.

    Attributes:
        xpath -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, xpath, message):
        self.xpath = xpath
        self.message = message
