from utils import config_properties

def launch_browser(driver):
    dev_url = config_properties.ReadConfig_CommonDetails().getDevUrl()
    driver.get(dev_url)
    # driver.maximize_window()
    # To maximize browser in the GitHub virtual machine
    driver.set_window_size(1920, 1080)

    return driver