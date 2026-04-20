import os
from src.pages.welcome_page import WelcomePage
from src.pages.common_popups import CommonPopups
from src.pages.login_page import LoginPage
from src.pages.otp_page import OtpPage
from src.pages.home_page import HomePage
from src.core.base_page import BasePage

DEMO_HP = os.getenv("DEMO_HP", "85225621673")
DEMO_OTP = os.getenv("DEMO_OTP", "123456")

def test_login_to_home(driver):
    base = BasePage(driver)
    base.ensure_app_foreground()

    WelcomePage(driver).complete_welcome(max_steps=3)
    CommonPopups(driver).grant_runtime_permissions(max_prompts=4)

    LoginPage(driver).login(DEMO_HP)
    OtpPage(driver).submit_otp(DEMO_OTP)

    home = HomePage(driver)
    if not home.wait_until_loaded(timeout=30):
        base.dump_debug(prefix="HOME_NOT_FOUND")
        assert False, "Gagal login ke homepage (cek artifacts/)."