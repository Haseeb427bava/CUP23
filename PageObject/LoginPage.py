"""Here the library and registration package are imported"""
from selenium.webdriver.common.by import By
from PageObject.RegistrationPage import RegistrationPage

"""Login Page POM Class to manage the login page elements"""


class LoginPage:
    """This function is used to pass drivers between browser and framework"""
    def __init__(self, driver):
        self.driver = driver

    """XPATH of the Elements of Login Page like email, password, signin, signup, forget password and invalid message"""
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "react-password")
    SIGNIN_BUTTON = (By.ID, "login-submit")
    SIGNUP_LINK_TEXT = (By.PARTIAL_LINK_TEXT, "Sign Up")
    FORGET_PASS = (By.PARTIAL_LINK_TEXT, "Password")
    INVALID_MSG = (By.XPATH, '//*[@id="react-password-helper-text"]')

    """The functions are getting driver and finding elements using BY library"""

    """Email"""
    def get_email(self):
        return self.driver.find_element(*LoginPage.EMAIL_FIELD)

    """Password"""
    def get_password(self):
        return self.driver.find_element(*LoginPage.PASSWORD_FIELD)

    """Signin-Button"""
    def click_signin_button(self):
        return self.driver.find_element(*LoginPage.SIGNIN_BUTTON)

    """SignUp for assertion"""
    def signup_link_text(self):
        return self.driver.find_element(*LoginPage.SIGNUP_LINK_TEXT)

    """SignUp Click to land on registration page"""
    def click_signup_link_text(self):
        self.driver.find_element(*LoginPage.SIGNUP_LINK_TEXT).click()
        registration_page = RegistrationPage(self.driver)
        return registration_page

    """Forget password msg"""
    def forget_password(self):
        return self.driver.find_element(*LoginPage.FORGET_PASS)

    """Forget password msg"""
    def invalid_msg(self):
        return self.driver.find_element(*LoginPage.INVALID_MSG)
