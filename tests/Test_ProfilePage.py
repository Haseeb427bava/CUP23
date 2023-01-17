import time
import pytest
from TestData.Data import Data
from Utilities.BaseClass import BaseClass
from tests.Functions.Login import Login

"""class for assertion and no of test cases"""


class TestProfile(BaseClass):
    """Login tests and their assertion"""

    def test_profile(self, getData, gotData):
        login = Login(self.driver)
        login.get_login(getData)
        time.sleep(1)



@pytest.fixture(params=Data.Login_data)
def getData(request):
    return request.param


@pytest.fixture(params=Data.Profile_Data)
def getData(request):
    return request.param
