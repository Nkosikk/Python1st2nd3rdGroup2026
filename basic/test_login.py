from telnetlib import EC

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin:

    website_url = "https://ndosisimplifiedautomation.vercel.app/"
    main_login_button_xpath = "//div[@class='nav-user-section']"
    username_id = "login-email"
    password_id = "login-password"
    login_button_id = "login-submit"
    verify_dashboard_content_xpath = "//h2"


    def test_login(self):
        #start the browser and navigate to the website
        options = Options()
        options.add_argument("--headless=new")  # modern headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")  # Additional flag for CI stability
        self.driver = webdriver.Chrome(options)
        self.driver.get(self.website_url)
        self.driver.set_window_size(1920, 1080)

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.main_login_button_xpath))).click()
        self.driver.find_element(By.ID, self.username_id).send_keys("nkwanyana@gmail.com")
        self.driver.find_element(By.ID, self.password_id).send_keys("#12345678")
        self.driver.find_element(By.ID, self.login_button_id).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, self.verify_dashboard_content_xpath))).is_displayed()

        self.driver.close()



