from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.core.base_page import BasePage

class HomePage(BasePage):
    _HOME_CANDIDATES = [
        (AppiumBy.XPATH, '//android.view.View[@content-desc="Info Akun"]'),
    ]

    def wait_until_loaded(self, timeout=30):
        print("[HOME] Sedang memindai elemen Home (Info Akun)...")
        found_element = self.wait_any_visible(self._HOME_CANDIDATES, timeout=timeout)

        if found_element:
            try:
                txt = found_element.text or found_element.get_attribute("content-desc")
                print(f"[HOME] Berhasil masuk Home Page. Elemen ditemukan dengan teks: '{txt}'")
            except Exception:
                print(f"[HOME] Berhasil masuk Home Page. Elemen ditemukan.")
            return True
        else:
            print("[HOME] Gagal menemukan elemen Home Page dalam batas waktu.")
            return False