import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def setup(browser):

    #Initialize the WebDriver based on the browser name provided
    if browser.lower() == "chrome":
        options = Options()
        options.add_argument("--headless=new")  # modern headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")  # Additional flag for CI stability
        driver = webdriver.Chrome(options=options)

    elif browser.lower() == "edge":
        driver = webdriver.Edge()

    elif browser.lower() == "Safari":
        driver = webdriver.Safari()

    else:
        driver = webdriver.Firefox()

    # Yield the WebDriver instance and ensure cleanup
    yield driver
    driver.quit()


def pytest_addoption(parser):
    # Add a command-line option "--browser" to specify the browser
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")
