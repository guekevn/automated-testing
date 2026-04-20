import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def find (self, locator_tuple):
        return self.driver.find_element(*locator_tuple)
    
    def click (self, locator_tuple):
        element = self.wait.until(EC.element_to_be_clickable(locator_tuple))
        element.click()

    def input_text (self, locator_tuple, text):
        element = self.wait.until(EC.visibility_of_element_located(locator_tuple))
        element.clear()
        element.send_keys(text)
    
    def is_visible (self, locator_tuple, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator_tuple))
            return True
        except TimeoutException:
            return False

    def ensure_app_foreground(self, app_package=None):
        """Memastikan aplikasi berada di latar depan. Jika app_package kosong, gunakan dari .env."""
        if app_package is None:
            app_package = os.getenv("APP_PACKAGE", "com.mkp.mitra_mint")

        try:
            current_app = self.driver.current_package
            if current_app != app_package:
                self.driver.activate_app(app_package)
                print(f"[INFO] App {app_package} activated.")
        except WebDriverException as e:
            print(f"[WARN] Failed to ensure app is foreground: {e}")

    def dump_debug(self, prefix="DEBUG"):
        """Menyimpan page source XML untuk debugging jika terjadi error."""
        try:
            filename = f"artifacts/{prefix}_source.xml"
            with open (filename, "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
            print(f"[DEBUG] Page source saved to {filename}")
        except Exception as e:
            print(f"[DEBUG] Failed to save page source: {e}")