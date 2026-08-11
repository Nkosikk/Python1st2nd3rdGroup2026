import pytest

from pageObjects.home_page import Home_page
from pageObjects.login_page import LoginPage
from utils.config_properties import ReadConfig_CommonDetails


class TestLogin:

    dev_url = ReadConfig_CommonDetails().getDevUrl()
    username = ReadConfig_CommonDetails().getUsername()
    password = ReadConfig_CommonDetails().getPassword()

    @pytest.mark.sanity
    def test_valid_login(self, setup):
        self.driver = setup
        self.driver.get(self.dev_url)

        home = Home_page(self.driver)
        home.click_main_login_button()

        login = LoginPage(self.driver)
        login.getUsername(self.username)
        login.getPassword(self.password)
        login.clickLoginButton()
