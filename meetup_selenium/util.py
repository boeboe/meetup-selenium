"""
Module with helper functions
"""
import inspect

def print_pretty(*args):
    """Function to print messages with the file source of the message """
    frame = inspect.stack()[1]
    filepath = frame[0].f_code.co_filename
    filename = filepath.split("/")[-1]
    print("[" + filename + "]", *args)

def yes_or_no(question):
    """Function to wait for a yes or no answer and proceed of yet, exit if no """
    while "the answer is invalid":
        reply = str(input(question+' (y/n)? ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False
