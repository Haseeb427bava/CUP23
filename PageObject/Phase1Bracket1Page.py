"""it manages all the properties in the home page"""
from selenium.webdriver.common.by import By


class CatsFormPage:
    def __init__(self, driver):
        self.driver = driver

    HEADING = (By.CSS_SELECTOR, '//*[@id="main"]/form/div/div[1]/div/h1')
    PARAGRAPH = (By.XPATH, '//*[@id="main"]/form/div/div[2]//*[@id="main"]/form/div/div[2]')
    RICH_TEXT = (By.CSS_SELECTOR, '//*[@id="main"]/form/div/div[3]/div/div/div[2]/div[3]/div')

    STORY = (By.CSS_SELECTOR, '//*[@id="main"]/form/div/div[4]/div/div/div[2]/div[3]/div')
    PICTURE = (By.CSS_SELECTOR, '//*[@id="main"]/form/div/div[5]/div/div/div[3]/label')
    PRODUCT_FILE = (By.XPATH, '//*[@id="main"]/form/div/div[6]/div/div/div[3]/label')
    HABITS_CHECK_BOX = (By.XPATH, '//*[@id="main"]/form/div/div[7]/div/fieldset/div/label/span[1]')
    GAMES_CHECK_BOX = (By.XPATH, '//*[@id="main"]/form/div/div[8]/div/fieldset/div/label/span[1]')
    TOWN_RADIO_BUTTONS = (By.XPATH, '//*[@id="main"]/form/div/div[9]/div/div/div[2]/label/span[1]/span[1]/input')
    CITY_RADIO_BUTTONS = (By.XPATH, '//*[@id="main"]/form/div/div[10]/div/div/div[2]/label/span[1]/span[1]/input')
    PROVINCE_DROPDOWN = (By.XPATH, '//*[@id="mui-component-select-select88153"]')
    AREA_DROPDOWN = (By.XPATH, '//*[@id="category-select"]')
    MESSAGE = (By.XPATH, '//*[@id="category-select"]')
    ANYTHING_NEW = (By.XPATH, '//*[@id="category-select"]')
    PROFILE_URL = (By.XPATH, '//*[@id="category-select"]')
    SPECIALITY = (By.XPATH, '//*[@id="category-select"]')
    PRODUCT = (By.XPATH, '//*[@id="category-select"]')
    SAVE_BUTTON = (By.XPATH, '//*[@id="category-select"]')
    DOWNLOAD_BUTTON = (By.XPATH, '//*[@id="category-select"]')
    UN_SUBMIT_BUTTON = (By.XPATH, '//*[@id="category-select"]')


    """"""

    def form_assertion(self):
        return self.driver.find_element(*CatsFormPage.CATEGORY_SELECT)

    def form_title_submission(self):
        return self.driver.find_element(*CatsFormPage.TITLE_SUBMISSION)

    def form_test_field1(self):
        return self.driver.find_element(*CatsFormPage.TEST_FIELD1)

    def form_test_field2(self):
        return self.driver.find_element(*CatsFormPage.TEST_FIELD2)

    def rich_text(self):
        return self.driver.find_element(*CatsFormPage.TEST_RICH)

    def about_cat(self):
        return self.driver.find_element(*CatsFormPage.ABOUT_CAT)

    def youtube_url(self):
        return self.driver.find_element(*CatsFormPage.YOUTUBE_URL)

    def cat_checkbox(self):
        return self.driver.find_element(*CatsFormPage.CAT_FORM_CHECKBOX)

    def cat_radio_button(self):
        return self.driver.find_element(*CatsFormPage.CAT_RADIO_BUTTON)

    def cat_text(self):
        return self.driver.find_elements(*CatsFormPage.TEXT)
