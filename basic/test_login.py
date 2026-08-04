from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    website_url = "https://ndosisimplifiedautomation.vercel.app/"
    main_login_button_xpath = "//div[@class='nav-user-section']"
    username_id = "login-email"
    password_id = "login-password"
    login_button_id = "login-submit"

    def test_login(self):
        #start the browser and navigate to the website
        self.driver = webdriver.Chrome()
        self.driver.get(self.website_url)

        wait = WebDriverWait(self.driver, 10)
