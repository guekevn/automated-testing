from appium import webdriver
from pathlib import Path
from appium.options.android import UiAutomator2Options

def driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.udid = '1902390100180748'
    options.platform_version = '10.0'
    options.device_name = 'Android'
    options.app = str(Path(__file__).parent.joinpath('src/app/LOKET MINT_1.24.06.02_Production.apk'))
    options.automation_name = 'UiAutomator2'
    options.auto_grant_permissions = True
    options.new_command_timeout = 1200000
    
    driver_instance = webdriver.Remote('http://localhost:4723', options=options)
    return driver_instance

