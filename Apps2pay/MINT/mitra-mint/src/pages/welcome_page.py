from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from src.core.base_page import BasePage

class WelcomePage(BasePage):
    BTN_NEXT = (AppiumBy.ID, "new UiSelector().description(\"Lanjutkan\")")
    BTN_SKIP = (AppiumBy.ID, "new UiSelector().description(\"Masuk/Daftar\")")
    def complete_welcome(self, max_steps=3):
        print("[STEP] Completing welcome screens...")
        for _ in range(max_steps):
            if self.is_visible(self.BTN_NEXT, timeout=5):
                self.click(self.BTN_NEXT)
            if self.is_visible(self.BTN_SKIP, timeout=5):
                self.click(self.BTN_SKIP)
                break
            else :
                break
