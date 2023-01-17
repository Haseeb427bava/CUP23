"""it manages all the properties in the profile page"""
from selenium.webdriver.common.by import By


class TeamPage:
    def __init__(self, driver):
        self.driver = driver

    NAME_EDIT_BUTTON = (By.XPATH, '//*[@id="main"]/div[3]/div[1]/button')
    NAME = (By.XPATH, '//*[@id="main"]/div[3]/div[1]/div[1]/div/div/input')
    CONFIRM_TEAM_NAME = (By.XPATH, '//*[@id="main"]/div[3]/div[1]/div[2]/button')
    ADD_TEAM_BUTTON = (By.CSS_SELECTOR, "a[role='button']")
    FIRST_NAME = (By.XPATH, '//*[@id="main"]/div[3]/div[2]/form/div/div[1]/div[1]/div/div/input')
    LAST_NAME = (By.XPATH, '//*[@id="main"]/div[3]/div[2]/form/div/div[1]/div[2]/div/div/input')
    EMAIL_ADDRESS = (By.XPATH, '//*[@id="main"]/div[3]/div[2]/form/div/div[2]/div/div/input')
    MASSAGE = (By.XPATH, '//*[@id="main"]/div[3]/div[2]/form/div/div[3]/div/div/textarea')
    SAVE_BUTTON = (By.XPATH, '//*[@id="main"]/div[3]/div[2]/form/div/div[4]/button')
    DELETE_BUTTON = (By.XPATH, '//*[@id="main"]/div[3]/div[2]/div[2]/div/div[2]/button[3]')
    YES_BUTTON = (By.XPATH, '/html/body/div[4]/div[3]/div/div[3]/button[2]')

    def team_name_edit_butt(self):
        return self.driver.find_element(*TeamPage.NAME_EDIT_BUTTON)

    def team_name(self):
        return self.driver.find_element(*TeamPage.NAME)

    def confirm_team_name(self):
        return self.driver.find_element(*TeamPage.CONFIRM_TEAM_NAME)

    def add_team_member(self):
        return self.driver.find_element(*TeamPage.ADD_TEAM_BUTTON)

    def team_member_first_name(self):
        return self.driver.find_element(*TeamPage.FIRST_NAME)

    def team_member_last_name(self):
        return self.driver.find_element(*TeamPage.LAST_NAME)

    def team_member_email(self):
        return self.driver.find_element(*TeamPage.EMAIL_ADDRESS)

    def team_member_save_button(self):
        return self.driver.find_element(*TeamPage.SAVE_BUTTON)

    def team_member_message(self):
        return self.driver.find_element(*TeamPage.MASSAGE)

    def team_delete_button(self):
        return self.driver.find_element(*TeamPage.DELETE_BUTTON)

    def team_yes_button(self):
        return self.driver.find_element(*TeamPage.YES_BUTTON)
