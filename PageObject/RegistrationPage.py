"""it manages all the Properties in the Registration page"""
from selenium.webdriver.common.by import By

from PageObject.ThankPage import ThankYouPage


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    """Elements of Registration_Page"""
    First_Name = (By.XPATH, '//*[@id="reactRegister"]/form/div[3]/div/div/div[2]/div/input')
    CHECK_BOX_reading = (By.XPATH, "//input[@value='Reading']")
    CHECK_BOX_writing = (By.XPATH, "//input[@value='Writing']")
    CHECK_BOX_playing = (By.XPATH, "//input[@value='Playing']")
    LAST_NAME = (By.XPATH, '//*[@id="reactRegister"]/form/div[5]/div/div/div[2]/div/input')
    TEAM_NAME = (By.XPATH, '//*[@id="reactRegister"]/form/div[6]/div/div/div[2]/div/input')
    EMAIL = (By.XPATH, '//*[@id="reactRegister"]/form/div[7]/div/div/div[2]/div/input')
    CREATE_PASSWORD = (By.XPATH, '//*[@id="reactRegister"]/form/div[8]/div/div/div[2]/div/input')
    CONFIRM_PASSWORD = (By.XPATH, '//*[@id="reactRegister"]/form/div[9]/div/div/div[2]/div/input')
    SIGNUP_BUTTON = (By.CLASS_NAME, 'MuiButton-label')


    """the functions assert the signup text email, password and clicking on button"""
    """First Name"""

    def give_first_name(self):
        return self.driver.find_element(*RegistrationPage.First_Name)

    def select_check_box_reading(self):
        return self.driver.find_element(*RegistrationPage.CHECK_BOX_reading)

    def select_check_box_writing(self):
        return self.driver.find_element(*RegistrationPage.CHECK_BOX_writing)

    def select_check_box_playing(self):
        return self.driver.find_element(*RegistrationPage.CHECK_BOX_playing)
    """Last Name"""
    def give_last_name(self):
        return self.driver.find_element(*RegistrationPage.LAST_NAME)
    """Password"""
    def give_team_name(self):
        return self.driver.find_element(*RegistrationPage.TEAM_NAME)
    """Invalid msg"""
    def give_email(self):
        return self.driver.find_element(*RegistrationPage.EMAIL)
    """Login-Button"""
    def give_create_password(self):
        return self.driver.find_element(*RegistrationPage.CREATE_PASSWORD)
    """"""
    def give_confirm_password(self):
        return self.driver.find_element(*RegistrationPage.CONFIRM_PASSWORD)

    def signup_button(self):
        return self.driver.find_element(*RegistrationPage.SIGNUP_BUTTON)

    def click_button(self):
        self.driver.find_element(*RegistrationPage.SIGNUP_BUTTON).click()
        thank_you_page = ThankYouPage(self.driver)
        return thank_you_page
