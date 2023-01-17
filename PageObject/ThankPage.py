from selenium.webdriver.common.by import By


class ThankYouPage:
    def __init__(self, driver):
        self.driver = driver

    THANKYOU_TEXT = (By.XPATH, '//*[@id="reactVerification"]/h1')

    """the functions assert the signup text email, password and clicking on button"""
    """First Name"""

    def thank_text(self):
        return self.driver.find_element(*ThankYouPage.THANKYOU_TEXT)