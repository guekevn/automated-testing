import pytest
import os
import subprocess
from appium import webdriver
from pathlib import Path
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def driver():
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.udid = '1902390100180748'
    options.device_name = 'Android'
    options.app = str(Path(__file__).parent.joinpath('app/LOKET MINT_1.24.06.02_Production.apk'))
    options.automation_name = 'UiAutomator2'
    options.auto_grant_permissions = True
    options.new_command_timeout = 1200000
    options.no_reset = False
    options.dont_stop_app_on_reset = True
    options.app_wait_activity = 'com.mkpmobile.retail.ui.SplashScreen'

    driver = webdriver.Remote('http://localhost:4723', options=options)

    yield driver

    driver.quit()

def pytest_sessionfinish(session, exitstatus):
    # Folder untuk hasil Allure
    allure_results_dir = 'allure-results'
    allure_report_dir = 'allure-report'

    # Buat folder jika belum ada
    if not os.path.exists(allure_results_dir):
        os.makedirs(allure_results_dir)

    # Hasilkan laporan Allure
    result = subprocess.run(['allure', 'generate', '--clean', allure_results_dir, '-o', allure_report_dir], capture_output=True, text=True)
    
    print(result.stdout)
    print(result.stderr)

    # Buka laporan Allure
    subprocess.run(['allure', 'open', allure_report_dir])
