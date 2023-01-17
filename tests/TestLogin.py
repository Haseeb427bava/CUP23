"""importing the BaseClass and Login class"""
import time
import pytest

from PageObject.LoginPage import LoginPage
from TestData.Data import Data
from Utilities.BaseClass import BaseClass
from tests.Functions.Login import Login


"""class for assertion and no of test cases"""


class TestContestantApp(BaseClass):
    """In this function we are testing login page with right and wrong credentials"""

    def test_login(self, getdata):
        login = Login(self.driver)
        login.get_wrong_login(getdata)
        login_page = LoginPage(self.driver)
        alert_text = login_page.invalid_msg().text
        assert ("You've" in alert_text)
        login.get_login(getdata)
        time.sleep(5)
        actual_url = self.driver.current_url
        expected_url = "https://cup23.skild.com/home"
        assert actual_url == expected_url


@pytest.fixture(params=Data.Login_data)
def getdata(request):
    return request.param
