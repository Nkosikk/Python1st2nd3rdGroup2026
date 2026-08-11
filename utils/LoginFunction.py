from pageObjects.home_page import Home_page
from pageObjects.login_page import LoginPage


def login(driver,username,password):
    homeP = Home_page(driver)
    loginP = LoginPage(driver)

    homeP.click_main_login_button()
    loginP.getUsername(username)
    loginP.getPassword(password)
    loginP.getLoginButton()