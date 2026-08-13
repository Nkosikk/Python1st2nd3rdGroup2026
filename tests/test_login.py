from time import sleep

import allure
import pytest

from pageObjects.home_page import Home_page
from pageObjects.login_page import LoginPage
from utils.LoginFunction import login
from utils.config_properties import ReadConfig_CommonDetails
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.dashboard_page import dashboard_page

from utils.launchBrowser import launch_browser


class TestLogin:

    dev_url = ReadConfig_CommonDetails().getDevUrl()
    username = ReadConfig_CommonDetails().getUsername()
    password = ReadConfig_CommonDetails().getPassword()
    invalid_username = ReadConfig_CommonDetails().getInvalidUsername()
    invalid_password = ReadConfig_CommonDetails().getInvalidPassword()

    @pytest.mark.sanity
    def test_valid_login(self, setup):

        self.driver = launch_browser(setup)
        login(self.driver, self.username, self.password)
        dashboard = dashboard_page(self.driver)
        dashboard.verify_dashboard_page()
        sleep(10)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Positive", attachment_type=allure.attachment_type.PNG)

    @pytest.mark.sanity
    def test_invalid_login(self, setup):
        self.driver = launch_browser(setup)
        login(self.driver, self.invalid_username, self.invalid_password)
        wait = WebDriverWait(self.driver, 10)
        alert = wait.until(EC.alert_is_present())
        alert.accept()
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Negative",attachment_type=allure.attachment_type.PNG)





