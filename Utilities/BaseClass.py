import inspect
import logging
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.LINK_TEXT, text)))
        element.click()

    def click_link(self, text):
        self.driver.find_element(By.LINK_TEXT, text).click()

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_index(text)

    def selectCheckBox(self, locator, text):
        for data in locator:
            if data.text == text:
                data.click()

    def sending_key(self, locator: object, text: object) -> object:
        locator.click()
        locator.send_keys(Keys.CONTROL, "a", Keys.DELETE)

        locator.send_keys(text)
