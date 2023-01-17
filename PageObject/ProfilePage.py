"""it manages all the properties in the profile page"""
from selenium.webdriver.common.by import By


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    """Web_Elements of profile_page"""
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input[name$='firstName']")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input[name='lastName']")
    NAME_UPDATE_BUTTON = (By.XPATH, '//*[@id="main"]/div[2]/div[2]/form/div/div[4]/button')
    NEW_EMAIL = (By.CSS_SELECTOR, "input[name='newEmail']")
    CONFIRM_EMAIL = (By.CSS_SELECTOR, "input[name='confirmEmail']")
    CHANGE_EMAIL_BUTTON = (By.PARTIAL_LINK_TEXT, '//*[@id="main"]/div[2]/div[3]/form/div/div[4]/button/span[1]')
    NEW_PASSWORD = (By.ID, "newPassword")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input[name='confirmPassword']")
    CHANGE_PASSWORD_BUTTON = (By.PARTIAL_LINK_TEXT, '//*[@id="main"]/div[2]/div[4]/form/div/div[3]/button')

    def profile_first_name(self):
        return self.driver.find_element(*ProfilePage.FIRST_NAME_FIELD)

    def profile_last_name(self):
        return self.driver.find_element(*ProfilePage.LAST_NAME_FIELD)

    def profile_name_update_button(self):
        return self.driver.find_element(*ProfilePage.NAME_UPDATE_BUTTON)

    def profile_new_email(self):
        return self.driver.find_element(*ProfilePage.NEW_EMAIL)

    def profile_confirm_email(self):
        return self.driver.find_element(*ProfilePage.CONFIRM_EMAIL)

    def profile_email_change_button(self):
        return self.driver.find_element(*ProfilePage.CHANGE_EMAIL_BUTTON)

    def profile_new_password(self):
        return self.driver.find_element(*ProfilePage.NEW_PASSWORD)

    def profile_confirm_password(self):
        return self.driver.find_element(*ProfilePage.CONFIRM_PASSWORD)

    def profile_password_change_button(self):
        return self.driver.find_element(*ProfilePage.CHANGE_PASSWORD_BUTTON)
