"""importing the class LoginPage"""
import time
from PageObject.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass

"""Declared the class"""


class Registration(BaseClass):
    """constructor for passing the drivers"""

    def __init__(self, driver):
        self.driver = driver

    """Correct Registration"""

    def wrong_registration(self, getdata):
        self.driver.implicitly_wait(5)
        login = LoginPage(self.driver)
        registration_page = login.click_signup_link_text()
        time.sleep(1)
        registration_page.give_first_name().send_keys(getdata["firstname"])
        registration_page.select_check_box_reading().click()
        registration_page.select_check_box_writing().click()
        registration_page.select_check_box_playing().click()
        time.sleep(1)
        registration_page.give_last_name().send_keys(getdata["lastname"])
        time.sleep(1)
        registration_page.give_team_name().send_keys(getdata["team_name"])
        time.sleep(1)
        registration_page.give_email().send_keys(getdata["email"])
        time.sleep(1)
        registration_page.give_create_password().send_keys(getdata["password"])
        time.sleep(1)
        registration_page.give_confirm_password().send_keys(getdata["password"])
        time.sleep(1)
        registration_page.signup_button().click()

    def correct_registration(self, getdata):
        # log = self.getLogger()
        self.driver.implicitly_wait(5)
        login = LoginPage(self.driver)
        time.sleep(1)
        registration_page = login.click_signup_link_text()
        time.sleep(1)
        registration_page.give_first_name().send_keys(getdata["firstname"])
        registration_page.select_check_box_reading().click()
        registration_page.select_check_box_writing().click()
        registration_page.select_check_box_playing().click()
        time.sleep(1)
        registration_page.give_last_name().send_keys(getdata["lastname"])
        time.sleep(1)
        registration_page.give_team_name().send_keys(getdata["team_name"])
        time.sleep(1)
        registration_page.give_email().send_keys(getdata["email"])
        time.sleep(1)
        registration_page.give_create_password().send_keys(getdata["password"])
        time.sleep(1)
        registration_page.give_confirm_password().send_keys(getdata["password"])
        time.sleep(1)
        registration_page.signup_button().click()
        registration_page.signup_button().Actions(self.driver)
        # registration_page.signup_button().send_keys(Keys.ENTER)
        time.sleep(10)
