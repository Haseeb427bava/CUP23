import time
from PageObject.TeamPage import TeamPage
from Utilities.BaseClass import BaseClass
from tests.Functions.Login import Login


class Team(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def team_page(self, getdata, got_data):
        login = Login(self.driver)
        login.get_login(getdata)
        time.sleep(1)
        team = TeamPage(self.driver)
        time.sleep(4)
        self.click_link("Team")
        team.team_name_edit_butt().click()
        self.sending_key(team.team_name(), got_data["team_name"])
        team.confirm_team_name().click()
        self.click_link("Add a Team Member")
        self.sending_key(team.team_member_first_name(), got_data["firstname"])
        self.sending_key(team.team_member_last_name(), got_data["lastname"])
        self.sending_key(team.team_member_email(), got_data["email"])
        self.sending_key(team.team_member_message(), got_data["message"])
        team.team_member_save_button().click()
