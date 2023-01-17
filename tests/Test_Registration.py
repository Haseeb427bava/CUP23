"""importing the Libraries, BaseClass and Login class"""
import pytest
from PageObject.ThankPage import ThankYouPage
from TestData.Data import Data
from Utilities.BaseClass import BaseClass
from tests.Functions.Registration import Registration

"""class for assertion and no of test cases"""


class TestContestantApp(BaseClass):
    def test_corrct_registration(self, got_data, getdata):
        registration = Registration(self.driver)
        registration.wrong_registration(got_data)
        thank_you_page = ThankYouPage(self.driver)
        alert_text = thank_you_page.thank_text().text
        assert ("Thank" not in alert_text)
        registration.correct_registration(getdata)
        assert ("Thank" in alert_text)

    @pytest.fixture(params=Data.Reg_Data)
    def getdata(self, request):
        return request.param

    # def test_wrong_registration(self, take_data):
    #     registration = Registration(self.driver)
    #     registration.correct_registration(take_data)
    #     current_title = self.driver.title
    #     expected_title = "Register"
    #     assert current_title == expected_title
    #     print(current_title)

    @pytest.fixture(params=Data.Reg_wrong_email_data)
    def got_data(self, request):
        return request.param
