from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:

    username_id = "login-email"
    password_id = "login-password"
    login_button_id = "login-submit"

    def __init__(self, driver):
        self.driver = driver

    def getUsername(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(self.driver.find_element_by_xpath(self.username_id)).send_keys(self.username_id)

    def getPassword(self):
        self.driver.find_element_by_xpath(self.password_id).send_keys(self.password_id)

    def getLoginButton(self):
        self.driver.find_element_by_xpath(self.login_button_id).click()