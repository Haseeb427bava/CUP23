import time
import pytest

from PageObject.HomePage import HomePage
from PageObject.Phase1Bracket1Page import CatsFormPage
from TestData.Data import Data
from Utilities.BaseClass import BaseClass
from tests.Functions.Home import Home
from tests.Functions.Login import Login

"""class for assertion and no of test cases"""


class TestHomepage(BaseClass):
    """Login tests and their assertion"""

    def test_home(self, getData, gotData):
        login = Login(self.driver)
        login.get_login(getData)
        time.sleep(1)
        # home = Home(self.driver)
        # home.homepage(gotData)
        # time.sleep(5)
        # form = CatsFormPage(self.driver)
        # ALERT_TEXT = form.form_assertion().text
        # assert (gotData["Bracket 1"] in ALERT_TEXT)
        home = HomePage(self.driver)
        assert (home.home_page_home_link().is_displayed())


@pytest.fixture(params=Data.Login_data)
def getData(request):
    return request.param


@pytest.fixture(params=Data.Dropdown_Data)
def gotData(request):
    return request.param
