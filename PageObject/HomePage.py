"""It manages all the properties on the home page"""
from PageObject.ApplicationPage import ApplicationPage
from PageObject.ProfilePage import ProfilePage
from PageObject.QuickLinks import QuickLinksPage
from PageObject.TeamPage import TeamPage

"""Here we importing libraries"""

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    HOME_LINK = (By.LINK_TEXT, "Home")
    PARAGRAPH = (By.LINK_TEXT, "Application")
    RICH_TEXT = (By.LINK_TEXT, "Team")
    STORY = (By.LINK_TEXT, "Profile")
    PICTURE = (By.PARTIAL_LINK_TEXT, "Quick")
    PRODUCT = (By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/div[1]/text()')
    CHECK_BOX = (By.CSS_SELECTOR, "main[id='main'] div div div h2")
    TIME_LEFT_TO_SUBMIT = (By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[1]/div[1]/div/div/p/span')
    PHASE_ONE = (By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[1]/div[2]/div/div/p/span[2]')
    DROP_DOWN = (By.XPATH, '//*[@id="category-select"]')
    BRACKETS = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li')
    BUTTON = (By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/button')

    """"""

    def home_page_home_link(self):
        return self.driver.find_element(*HomePage.HOME_LINK)

    def home_page_application_link(self):
        self.driver.find_element(*HomePage.APPLICATION_LINK)
        application_page = ApplicationPage(self.driver)
        return application_page

    def home_page_team_link(self):
        self.driver.find_element(*HomePage.TEAM_LINK)
        team_page = TeamPage(self.driver)
        return team_page

    def home_page_profile_link(self):
        self.driver.find_element(*HomePage.PROFILE_LINK)
        profile_page = ProfilePage(self.driver)
        return profile_page

    def homepage_quick_links(self):
        self.driver.find_element(*HomePage.QUICK_LINKS)
        quick_links = QuickLinksPage(self.driver)
        return quick_links

    def homepage_paragraph_text(self):
        return self.driver.find_element(*HomePage.PARAGRAPH_TEXT)

    def homepage_event_status(self):
        return self.driver.find_element(*HomePage.EVENT_STATUS)

    def homepage_time_left(self):
        return self.driver.find_element(*HomePage.TIME_LEFT_TO_SUBMIT)

    def homepage_phase_one(self):
        return self.driver.find_element(*HomePage.PHASE_ONE)

    def homepage_click_dropdown(self):
        return self.driver.find_element(*HomePage.DROP_DOWN)

    def homepage_bracket(self):
        return self.driver.find_element(*HomePage.BRACKETS)

    def homepage_button(self):
        return self.driver.find_element(*HomePage.BUTTON)
