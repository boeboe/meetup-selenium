"""Module to support parsing of meetup group pages """
import re

from .parseutil import *
from .exception import ParseError
from ..groupmember import GroupMember
from ..groupevent import GroupEvent

class GroupParser():
    """Class to interact with a group page """

    def __init__(self, driver):
        self.driver = driver

    def load_initial(self, url):
        """Load the group page """
        self.driver.get(url)

        xpath_page_loaded = '//div[contains(@class,"groupHomeHeader")]'
        wait_element(self.driver, xpath_page_loaded)

        if not get_element(self.driver, xpath_page_loaded):
            raise ParseError(xpath_page_loaded, "Unable to load group page")

    def join(self):
        """Join this group """
        if not self.get_joined():
            click_element(self.driver, '//a[text()="Join this group"]')
            wait_element(self.driver, '//button/span[text()="You\'re a member"]')

    def get_name(self):
        """Get the name of this group """
        return get_text(self.driver, '//a[contains(@class,"groupHomeHeader-groupNameLink")]')

    def get_location(self):
        """Get the location of this group """
        return get_text(self.driver, '//a[contains(@class,"groupHomeHeaderInfo-cityLink")]/span')

    def get_joined(self):
        """Get joined status of this group (True or False) """
        return (not has_element(self.driver, '//a[text()="Join this group"]')) and \
                has_element(self.driver, '//button/span[text()="You\'re a member"]')

    def get_member_count(self):
        """Get the number of members of this group """
        res = get_text(self.driver, '//a[@class="groupHomeHeaderInfo-memberLink"]/span')
        result = res.split()[0].replace(",", "")
        return int(result)

    def get_description(self):
        """Get the description of this group """
        read_more = self.get_btn_read_more()
        if read_more:
            read_more.click()
        return get_text(self.driver, '//section[@id="overview"]/div/div')

    def get_btn_read_more(self):
        """Get the read more button on this page """
        return get_element(self.driver, '//button[text()="Read more"]')

    def get_menu_about(self):
        """Get the about menu on this page """
        return get_element(self.driver, '//a/span[text()="About"]')

    def get_menu_events(self):
        """Get the events menu on this page """
        return get_element(self.driver, '//a/span[text()="Events"]')

    def get_menu_members(self):
        """Get the members menu on this page """
        return get_element(self.driver, '//a/span[text()="Members"]')

    def get_menu_photos(self):
        """Get the photos menu on this page """
        return get_element(self.driver, '//a/span[text()="Photos"]')

    def get_menu_discussions(self):
        """Get the discussions menu on this page """
        return get_element(self.driver, '//a/span[text()="Discussions"]')


    def get_members(self):
        """Get the members of this group """
        members = []
        self.get_menu_members().click()

        wait_element(self.driver, '//div[@id = "member-list-card-id"]')
        wait_element(self.driver, '//div[span="All members"]/following-sibling::div/span')
        members_section = get_element(self.driver, '//div[@id = "member-list-card-id"]')

        total_member_count_string = get_text(self.driver, '//div[span="All members"]/following-sibling::div/span')
        total_member_count = int(total_member_count_string.replace(",", ""))
        current_member_count = 0

        while current_member_count < total_member_count:
            load_full_page(self.driver)
            time.sleep(0.1)

            if has_element(members_section, './/button[@class = "infiniteScrollLoadMoreButton"]'):
                click_element(members_section, './/button[@class = "infiniteScrollLoadMoreButton"]')
                continue

            current_mem_elements = get_elements(members_section, './/li[contains(@class, "list-item")]')
            if current_mem_elements:
                current_member_count = len(current_mem_elements)

        final_members_section = get_element(self.driver, '//div[@id = "member-list-card-id"]')
        final_mem_elements = get_elements(final_members_section, './/li[contains(@class, "list-item")]')
        for mem_element in final_mem_elements:
            name = get_text(mem_element, './/div[@class = "flex-item _memberItem-module_name__BSx8i"]//a')
            url = get_attribute(mem_element, './/div[@class = "flex-item _memberItem-module_name__BSx8i"]//a', 'href')
            user_id = re.search('members/(.*)/profile', url).group(1)
            joined = get_text(mem_element, './/span[contains(text(), "Joined")]')
            members.append(GroupMember(name=name, url=url, user_id=user_id, joined=joined))

        return members


    def get_upcoming_events(self):
        """Get the upcoming events of this group """
        events = []
        self.get_menu_events().click()

        wait_element(self.driver, '//span[text()="Upcoming"]')
        get_element(self.driver, '//span[text()="Upcoming"]').click()

        wait_element(self.driver, '//ul[contains(@class, "eventList-list")]')
        for event_item in get_elements(self.driver, '//li[contains(@class, "list-item")]'):
            name = get_text(event_item, './/a[@class="eventCardHead--title"]')
            url = get_attribute(event_item, './/a[@class="eventCard--link"]', "href")
            date = get_text(event_item, './/span[@class="eventTimeDisplay-startDate"]')
            location = get_text(event_item, './/address/p')
            descr = get_text(event_item, './/div[div[@class="eventCardHead"]]/following-sibling::div/div/div/div/p[2]')
            cnt_attendees_raw = get_text(event_item, './/li[contains(@class,"avatarRow--attendingCount")]')
            cnt_attendees = int(cnt_attendees_raw.split()[0].replace(",", ""))

            events.append(GroupEvent(name=name, url=url, date=date, location=location, description=descr,
                                     cnt_attendees=cnt_attendees))

        return events
