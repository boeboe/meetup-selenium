"""Module to with helper functions for selenium browser interaction """
import time

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from ..util import print_pretty

def load_full_page(root, timeout=1):
    """Scroll to the bottom of the page to load the full page """
    root.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight));")
    time.sleep(timeout)
    root.execute_script("window.scrollTo(0, 0);")

def load_infinite_page(root, xpath_list, xpath_more, retries=5, timeout=2):
    """Scroll to the bottom of the page and press "more items" until all items are loaded """
    count = len(get_elements(root, xpath_list))
    done_count = 0

    while True:
        load_full_page(root, timeout=timeout)
        if has_element(root, xpath_more):
            click_element(root, xpath_more)

        if len(get_elements(root, xpath_list)) > count:
            count = len(get_elements(root, xpath_list))
            done_count = 0
            continue
        else:
            done_count += 1

        if done_count >= retries:
            break

def wait_page_loaded(root, url, timeout=1, tries=10):
    """Wait for a page to be loaded by verifying the current URL """
    print_pretty("Waiting for page", url, "to be loaded")
    count = 1
    while True:
        if count >= tries:
            return

        current_url = root.current_url
        if current_url == url:
            break
        time.sleep(timeout)

def wait_element(root, xpath, timeout=1, tries=10):
    """Wait for an element """
    print_pretty("Waiting to find element", xpath)
    count = 1
    while True:
        if count >= tries:
            input()
            print_pretty("Unable to find element", xpath)
            return

        try:
            root.find_element_by_xpath(xpath)
            break
        except NoSuchElementException:
            count += 1
            time.sleep(timeout)
            continue

def wait_element_clickable(root, xpath, timeout=1, tries=10):
    """Wait for an element to become clickable """
    count = 1
    while True:
        if count >= tries:
            break

        try:
            root.find_element_by_xpath(xpath)
            wait = WebDriverWait(root, timeout)
            wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            break
        except NoSuchElementException:
            count += 1
            time.sleep(0.1)
            continue

def get_element(root, xpath):
    """Get a webelement by XPATH """
    try:
        element = root.find_element_by_xpath(xpath)
        return element
    except NoSuchElementException:
        return None

def get_elements(root, xpath):
    """Get a list of webelements by XPATH """
    try:
        elements = root.find_elements_by_xpath(xpath)
        return elements
    except NoSuchElementException:
        return []

def print_element(root, xpath):
    """Print the outer HTML from a webelement by XPATH """
    try:
        element = root.find_element_by_xpath(xpath)
        print_pretty(element.get_attribute("outerHTML"))
        return element
    except NoSuchElementException:
        return None

def get_text(root, xpath):
    """Get the text of a webelement by XPATH """
    try:
        element = root.find_element_by_xpath(xpath)
        return element.text
    except NoSuchElementException:
        return None

def get_texts(root, xpath):
    """Get a list of texts of webelements by XPATH """
    texts = []
    try:
        elements = lambda: root.find_elements_by_xpath(xpath)
        for element in elements():
            texts.append(element.text)
    except NoSuchElementException:
        pass
    return texts

def get_attribute(root, xpath, attr):
    """Get the attribute of a webelement by XPATH """
    try:
        element = root.find_element_by_xpath(xpath)
        return element.get_attribute(attr)
    except NoSuchElementException:
        return None

def get_attributes(root, xpath, attr):
    """Get a list of attributes of webelements by XPATH """
    attributes = []
    try:
        for element in root.find_elements_by_xpath(xpath):
            attributes.append(element.get_attribute(attr))
    except NoSuchElementException:
        pass
    return attributes

def has_element(root, xpath):
    """Check if a webelement is present """
    try:
        root.find_element_by_xpath(xpath)
        return True
    except NoSuchElementException:
        return False

def click_element(root, xpath):
    """Click a webelement """
    try:
        element = root.find_element_by_xpath(xpath)
        element.click()
    except NoSuchElementException:
        pass

def click_elements(root, xpath):
    """Click a list of webelements """
    try:
        for element in root.find_elements_by_xpath(xpath):
            try:
                element.click()
            except ElementNotInteractableException:
                continue
    except NoSuchElementException:
        pass
