import pytest
import os
import subprocess
from appium import webdriver
from pathlib import Path
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="session")
def driver(request):
    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.udid = '1902390100180748'
    options.device_name = 'Android'
    options.app = str(Path(__file__).parent.joinpath('app/LOKET MINT_1.24.09.02_Production.apk'))
    options.automation_name = 'UiAutomator2'
    options.auto_grant_permissions = True
    options.new_command_timeout = 300
    options.no_reset = False
    options.dont_stop_app_on_reset = True
    options.app_wait_activity = 'com.mkpmobile.retail.ui.SplashScreen'
    
    driver_instance = webdriver.Remote('http://localhost:4723', options=options)

    def tearDown():
        yield driver_instance
    
    request.addfinalizer(tearDown)
    return driver_instance

# def pytest_sessionfinish(session, exitstatus):
#     # Folder untuk hasil Allure
#     allure_results_dir = 'allure-results'
#     allure_report_dir = 'allure-report'

#     # Buat folder jika belum ada
#     if not os.path.exists(allure_results_dir):
#         os.makedirs(allure_results_dir)

#     # Hasilkan laporan Allure
#     try:
#         result = subprocess.run(
#             ['allure', 'generate', '--clean', allure_results_dir, '-o', allure_report_dir],
#             capture_output=True, text=True, check=True
#         )
#         print("Allure report generated successfully!")
#         print(result.stdout)
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to generate Allure report: {e}")
#         print(e.stdout)
#         print(e.stderr)

#     # Buka laporan Allure
#     try:
#         subprocess.run(['allure', 'open', allure_report_dir], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Failed to open Allure report: {e}")