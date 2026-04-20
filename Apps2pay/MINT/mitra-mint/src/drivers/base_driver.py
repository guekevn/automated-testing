import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

# load env variables
load_dotenv()

def init_driver():
    options = UiAutomator2Options()
    
    # Mapping capabilities dari .env
    options.platform_name = os.getenv("PLATFORM_NAME")
    options.platform_version = os.getenv("PLATFORM_VERSION")
    options.device_name = os.getenv("DEVICE_NAME")
    options.app_package = os.getenv("APP_PACKAGE")
    options.app_activity = os.getenv("APP_ACTIVITY")
    options.app_path = os.getenv("APP_PATH")

    # Tambahan capabilities
    options.automation_name = "UiAutomator2"
    options.no_reset = True


    server_url = os.getenv("APPIUM_SERVER", "http://127.0.0.1:4723")
    
    print(f"[INIT] connecting to Appium server : {server_url}...")
    driver = webdriver.Remote(server_url, options=options)
    driver.implicitly_wait(10)
    return driver