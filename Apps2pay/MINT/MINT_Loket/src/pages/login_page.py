from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_next_button(self):
        wait = WebDriverWait(self.driver, 10)
        for _ in range(3):
            next_button = wait.until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/btnNext')))
            next_button.click()

    def set_cid(self, cid):
        cid_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/edCid')))
        cid_field.send_keys(cid)

    def set_username(self, username):
        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/edUsser')))
        username_field.send_keys(username)

    def set_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/edPassword')))
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/btnLogin')))
        login_button.click()

    def wait_for_home_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/action_bar_root')))
