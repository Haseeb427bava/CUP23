"""Importing libraries and packages"""
import time

import pytest
from PageObject.TeamPage import TeamPage
from TestData.Data import Data
from Utilities.BaseClass import BaseClass
from tests.Functions.AddTeamMember import Team

"""In this class we have tested the add team member page"""


class TestTeam(BaseClass):
    """This function is making team class object from functions package, and then we are calling team page function from
    Team class, and at the end we are asserting delete button"""

    def test_team(self, getdata, got_data):
        team_add = Team(self.driver)  # team object
        team_add.team_page(getdata, got_data)  # calling team_page function by using team object
        team = TeamPage(self.driver)  # This is the object of Team_Page
        button = team.team_delete_button()  # finding the delete button and storing it in a variable
        assert (button.is_displayed())  # asserting the delete button
        button.click()  # deleting the added team member
        team.team_yes_button().click() # handling the
        time.sleep(2)


@pytest.fixture(params=Data.Login_data)
def getdata(request):
    return request.param


@pytest.fixture(params=Data.Team_data)
def got_data(request):
    return request.param
