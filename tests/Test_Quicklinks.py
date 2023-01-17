import time
import pytest

from PageObject.QuickLinks import QuickLinksPage
from TestData.Data import Data
from Utilities.BaseClass import BaseClass
from tests.Functions.Login import Login

"""class for assertion and no of test cases"""


class TestQuicklinks(BaseClass):
    """Login tests and their assertion"""

    def test_Quicklinks(self,getData):
        login = Login(self.driver)
        login.get_login(getData)
        time.sleep(1)
        quicklinks = QuickLinksPage(self.driver)
        quicklinks.quick_links().click()
        quicklinks.test_universal().click()
        button = quicklinks.test_universal_assertion()
        assert (button.is_displayed())
        button.click()
        quicklinks.base_test().click()
        base_button = quicklinks.base_test_assertion()
        assert base_button.is_displayed
        base_button.click()


@pytest.fixture(params=Data.Login_data)
def getData(request):
    return request.param
