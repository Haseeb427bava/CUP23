"""it manages all the properties in the profile page"""
from selenium.webdriver.common.by import By


class ApplicationPage:
    def __init__(self, driver):
        self.driver = driver

    """Web_Elements of profile_page"""
    SENTENCE = (By.XPATH, "/html/body/div[4]/div[3]/div/div[1]/span")
    CLOSE_BUTTON = (By.XPATH, '//*[@id="root"]/div/nav/div[2]/div/div/div/ul/li[6]/div/div/div/ul/li[1]/div/button')
    DROPDOWN = (By.XPATH, '//*[@id="category-select"]')
    BRACKETS = (By.XPATH, '//*[@id="menu-"]/div[3]/ul')

    def quick_link_sentence(self):
        return self.driver.find_element(*ApplicationPage.SENTENCE)

    def quick_link_close_button(self):
        return self.driver.find_element(*ApplicationPage.CLOSE_BUTTON)

    def quick_link_dropdown(self):
        return self.driver.find_element(*ApplicationPage.DROPDOWN)

    def quick_link_bracket(self):
        return self.driver.find_element(*ApplicationPage.BRACKETS)
