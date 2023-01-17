import time
from PageObject.ProfilePage import ProfilePage
from Utilities.BaseClass import BaseClass


class Profile(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def profile_name(self, getdata):
        profile = ProfilePage(self.driver)
        time.sleep(4)
        self.sending_key(profile.profile_first_name(), getdata["First_Name"])
        self.sending_key(profile.profile_last_name(), getdata["Last_Name"])
        profile.profile_name_update_button().click()

    def profile_email(self, get_data):
        profile = ProfilePage(self.driver)
        time.sleep(4)
        self.sending_key(profile.profile_new_email(), get_data[""])
