"""it manages all the properties in the profile page"""
from selenium.webdriver.common.by import By


class QuickLinksPage:
    def __init__(self, driver):
        self.driver = driver

    """Web_Elements of profile_page"""
    QUICKLINKS = (By.XPATH, '//*[@id="root"]/div/nav/div[2]/div/div/div/ul/li[5]')
    TEST_UNIVERSAL = (By.XPATH, '//*[@id="root"]/div/nav/div[2]/div/div/div/ul/li[6]/div/div/div/ul/li[1]/div/button')
    TEST_UNIVERSAL_ASSERTION = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/button')
    BASE_TEST = (By.XPATH, '//*[@id="root"]/div/nav/div[2]/div/div/div/ul/li[6]/div/div/div/ul/li[2]/div/button')
    BASE_TEST_ASSERTION = (By.XPATH, '/html/body/div[4]/div[3]/div/div[1]/button')

    def quick_links(self):
        return self.driver.find_element(*QuickLinksPage.QUICKLINKS)

    def test_universal(self):
        return self.driver.find_element(*QuickLinksPage.TEST_UNIVERSAL)

    def test_universal_assertion(self):
        return self.driver.find_element(*QuickLinksPage.TEST_UNIVERSAL_ASSERTION)

    def base_test(self):
        return self.driver.find_element(*QuickLinksPage.BASE_TEST)

    def base_test_assertion(self):
        return self.driver.find_element(*QuickLinksPage.BASE_TEST_ASSERTION)
