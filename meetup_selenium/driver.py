"""Module to initialize selenium webdrivers """
import sys

# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.ie.options import Options as IeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

from .util import print_pretty

def connect_chrome_driver(headless):
    """Function to connect with chrome driver """
    #initialise chrome options
    options = ChromeOptions()
    #set headless option on driver
    options.headless = headless
    #initialise driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver

def connect_firefox_driver(headless):
    """Function to connect with firefox driver """
    #initialise chrome options
    options = FirefoxOptions()
    #set headless option on driver
    options.headless = headless
    #initialise driver
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    return driver

def connect_ie_driver(headless):
    """Function to connect with ie driver """
    #initialise chrome options
    options = IeOptions()
    #set headless option on driver
    options.headless = headless
    #initialise driver
    driver = webdriver.Ie(IEDriverManager().install(), options=options)
    return driver


def init_webdriver(driver_name=None, headless=False):
    """Function to initialize the webdriver """

    if driver_name == "chrome":
        try:
            #try to connect with chrome driver
            driver = connect_chrome_driver(headless)
        except:
            print_pretty("Sorry, you can't use chrome driver, please try another driver!")
            sys.exit(0)
    elif driver_name == "ie":
        try:
            #try to connect with ie driver
            driver = connect_ie_driver(headless)
        except:
            print_pretty("Sorry, you can't use internet explorer driver, please try another driver!")
            sys.exit(0)
    elif driver_name == "firefox":
        try:
            #try to connect with firefox driver
            driver = connect_firefox_driver(headless)
        except:
            print_pretty("sorry, you can't use firefox driver, please try another driver!")
            sys.exit(0)
    else:
        print_pretty("No browser selected, please choose 'chrome', 'ie' or 'firefox'")
        return None

    print_pretty("Selenium driver", driver_name, "sucessfully initialised")
    return driver
