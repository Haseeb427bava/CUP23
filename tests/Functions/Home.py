import time
from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class Home(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def homepage(self, gotData):
        homepage = HomePage(self.driver)
        time.sleep(4)
        homepage.homepage_click_dropdown().click()
        self.selectCheckBox(homepage.homepage_bracket(), gotData["Bracket 1"])
        time.sleep(4)
        homepage.homepage_button().click()
