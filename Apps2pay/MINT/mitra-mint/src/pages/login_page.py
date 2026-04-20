import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.core.base_page import BasePage

class LoginPage(BasePage):
    # Locator
    HP_FIELD = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
    CHECKBOX = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.CheckBox")')
    BTN_LOGIN = (AppiumBy.ACCESSIBILITY_ID, 'Masuk/Daftar')

    def login(self, hp: str):
        print(f"[LOGIN] Memulai login dengan nomor: {hp}")
        self.hide_keyboard()

        # 1. Input nomor HP
        self.wait_visible(self.HP_FIELD)
        self.robust_type_android(self.HP_FIELD, hp)
        self.hide_keyboard()

        # 2. Looping checkbox S&K
        max_retries = 5
        for i in range(max_retries):
            # 1. Ambil elemen tombol & checkbox
            btn = self.find_element(self.BTN_LOGIN)

            # Check status checkbox dengan aman
            try:
                cb = self.find_element(self.CHECKBOX)
                cb_val = cb.get_attribute("checked")
                is_checked = str(cb_val).lower() == "true"
            except Exception:
                is_checked = True  

            # Check status tombol
            is_btn_enabled = btn.get_attribute("enabled") == "true"

            print(f"[LOOP-{i+1}]Cek status UI -> Checkbox: {is_checked}, Tombol Enabled: {is_btn_enabled}")

            # KONDISI SUKSES: Checkbox True DAN Tombol True
            if is_checked and is_btn_enabled:
                print("[LOGIN] Checkbox sudah dicentang dan tombol aktif.")
                break
            
            # PERBAIKAN: Jika Checkbox BELUM True, Klik!
            if not is_checked:
                print("[LOGIN] Checkbox belum dicentang, mencoba centang...")
                cb.click()
                self.sleep(1)
                continue

            # PERBAIKAN: Jika Checkbox SUDAH True tapi Tombol masih False -> Input HP mungkin bermasalah
            if is_checked and not is_btn_enabled:
                print("[WARN] Checkbox oke tapi Tombol masih disable. Re-input HP...")
                self.robust_type_android(self.HP_FIELD, hp)
                self.hide_keyboard()
                self.sleep(1)


        # 3. EKSEKUSI : klik tombol Masuk/Daftar
        try:
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.BTN_LOGIN)
            )
            self.click(self.BTN_LOGIN)
            print("[LOGIN] Tombol Masuk/Daftar diklik.")
        except Exception as e:
            raise Exception(f"Gagal login! Tombol Masuk/Daftar tidak bisa diklik setelah {max_retries}x percobaan. Error: {e}, silahkan cek screenshot")