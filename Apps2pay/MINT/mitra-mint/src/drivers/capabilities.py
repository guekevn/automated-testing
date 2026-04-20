import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

# Memuat variable dari file .env
load_dotenv()

def get_capabilities():
    """
    Membaca konfigurasi dari file .env dan mengembalikannya sebagai UiAutomator2Options object.
    """
    caps = {
        "platformName"              : "Android",
        "automationName"            : "UiAutomator2",
        "platformVersion"           : os.getenv("PLATFORM_VERSION"),
        "deviceName"                : os.getenv("DEVICE_NAME"),
        "app"                       : os.getenv("APP_PATH"),
        "appPackage"                : "com.mkp.mitra_mint",
        "appActivity"               : "com.mkp.mitra_mint.MainActivity",
        "appWaitActivity"           : "com.mkp.mitra_mint.*",                 # longgar (sementara)
        "appWaitForLaunch"          : True,
        "appWaitDuration"           : 25000,   
        "newCommandTimeout"         : 300,   # 5 menit            # 25s
        "noReset"                   : False, # reset data tiap sesi test
        "fullReset"                 : False, # tidak install ulang app tiap sesi
        "autoGrantPermissions"      : True,
        "disableWindowAnimation"    : True,
        "ensureWebviewsHavePages"   : True,
    }

    # UiAutomator2Options untuk kompatibilitas Appium 2.0+
    options = UiAutomator2Options().load_capabilities(caps)

    app_path = os.getenv("APP_PATH")
    if app_path :
        abs_path = os.path.abspath(app_path)
        if os.path.exists(abs_path):
            caps["app"] = abs_path
        else:
            print(f"[Warning] App path tidak ditemukan: {abs_path}")
    return options