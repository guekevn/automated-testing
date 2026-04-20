from appium.webdriver.common.appiumby import AppiumBy
from src.core.base_page import BasePage

class OtpPage(BasePage):
    # Locator
    TITLE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().descriptionContains("Kode")')
    OTP_ONE_FIELD = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.EditText")')
    OTP_BOX = lambda self, i: (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().className("android.widget.EditText").instance({i})')

    def wait_otp_screen(self, timeout=15):
        # PERBAIKAN: Hanya return True jika JUDUL 'Kode' muncul.
        # Jangan pakai OTP_ONE_FIELD di sini karena Login Page juga punya EditText.
        return self.is_visible(self.TITLE, timeout=timeout)

    def submit_otp(self, code: str):
        # 1. Validasi Halaman yang Strict
        if not self.wait_otp_screen(timeout=20):
            # Jika judul tidak muncul, kita throw error.
            # Ini akan mencegah script lanjut ke Home Page check.
            raise Exception("Gagal masuk halaman OTP (Judul tidak ditemukan). Kemungkinan stuck di Login.")

        # 2. Input OTP
        if self.is_visible(self.OTP_ONE_FIELD, timeout=2):
            self.robust_type_android(self.OTP_ONE_FIELD, code)
        else:
            # Fallback 6 kotak
            for i, d in enumerate(code):
                box = self.OTP_BOX(i)
                self.robust_type_android(box, d)
        
        # 3. Auto-submit biasanya terjadi, atau ada tombol lanjut?
        # Jika ada tombol lanjut manual, tambahkan klik di sini.