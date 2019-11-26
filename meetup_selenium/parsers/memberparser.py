"""Module to support parsing of the meetup login page """
from .parseutil import *
from .exception import ParseError

class MemberParser():
    """Class to interact with a member detail page """

    def __init__(self, driver):
        self.driver = driver

    def load_initial(self, url):
        """Load the member page """
        self.driver.get(url)

        xpath_page_loaded = '//div[@id="D_groupMemberProfile"]'
        wait_element(self.driver, xpath_page_loaded, 1, 10)

        if not get_element(self.driver, xpath_page_loaded):
            raise ParseError(xpath_page_loaded, "Unable to load member details page")

    def get_name(self):
        """Get the name of this member """
        return get_text(self.driver, '//span[contains(@class,"memName")]')

    def get_location(self):
        """Get the location of this member """
        return get_text(self.driver, '//span[@class="locality"]')

    def get_date_joined(self):
        """Get the date of joining this group of this member """
        return get_text(self.driver, '//div[h4="Meetup member since:"]/p')

    def get_bio(self):
        """Get the biography of this member """
        if not has_element(self.driver, '//div[h4="Bio"]'):
            return None

        bio_tmp = get_text(self.driver, '//div[h4="Bio"]')
        bio = bio_tmp.split("\n")[1]
        return bio

    def get_facebook(self):
        """Get the facebook account of this member """
        if not has_element(self.driver, '//a[@title="Facebook"]'):
            return None

        return get_attribute(self.driver, '//a[@title="Facebook"]', "href")

    def get_twitter(self):
        """Get the twitter account of this member """
        if not has_element(self.driver, '//a[contains(@title,"Twitter:")]'):
            return None

        return get_attribute(self.driver, '//a[contains(@title,"Twitter:")]', "href")

    def get_flickr(self):
        """Get the flickr account of this member """
        if not has_element(self.driver, '//a[@title="Flickr"]'):
            return None

        return get_attribute(self.driver, '//a[@title="Flickr"]', "href")

    def get_tumblr(self):
        """Get the tumblr account of this member """
        if not has_element(self.driver, '//a[@title="Tumblr"]'):
            return None

        return get_attribute(self.driver, '//a[@title="Tumblr"]', "href")

    def get_interests(self):
        """Get the interests of this member """
        if not has_element(self.driver, '//div[@class="interest-topics"]//ul[@id="memberTopicList"]//a'):
            return []

        interests = get_texts(self.driver, '//div[@class="interest-topics"]//ul[@id="memberTopicList"]//a')
        return interests

    def get_groups(self):
        """Get the groups of this member """
        if has_element(self.driver, '//a[text()="See all my Meetup Groups"]'):
            btn_see_all_groups = get_element(self.driver, '//a[text()="See all my Meetup Groups"]')
            btn_see_all_groups.click()
            wait_element_clickable(self.driver, '//a[text()="Collapse"]', 1, 10)

        if not has_element(self.driver, '//div[@id="my-meetup-groups-list"]//h4/a'):
            return []

        groups = get_attributes(self.driver, '//div[@id="my-meetup-groups-list"]//h4/a', "href")
        return groups
