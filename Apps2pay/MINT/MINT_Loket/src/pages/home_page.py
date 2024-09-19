from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_hide_button(self):
        wait = WebDriverWait(self.driver, 10)
        for _ in range(3):
            hide_button = wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/showcase_button')))
            hide_button.click()
    
    def wait_for_homepage(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/action_bar_root')))