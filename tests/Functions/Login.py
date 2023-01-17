"""Here we are importing the library and package"""
import time
from PageObject.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass

"""Declared the class"""


class Login(BaseClass):
    """constructor for passing the drivers"""

    def __init__(self, driver):
        self.driver = driver

    """Here we are testing the login page with wrong credentials"""
    def get_wrong_login(self, getdata):
        self.driver.implicitly_wait(10)
        login = LoginPage(self.driver)
        login.get_email().send_keys(getdata["wrong_email"])
        login.get_password().send_keys(getdata["wrong_password"])
        login.click_signin_button().click()
        time.sleep(5)

    def get_login(self, getdata):
        self.driver.implicitly_wait(10)
        login = LoginPage(self.driver)
        self.sending_key(login.get_email(), getdata["email"])
        self.sending_key(login.get_password(), getdata["password"])
        login.click_signin_button().click()
        time.sleep(5)
