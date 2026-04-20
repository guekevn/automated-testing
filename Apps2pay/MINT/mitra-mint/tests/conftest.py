import os
import sys

# --- 1. PATH SETUP (WAJIB DI PALING ATAS) ---
# Ambil path folder 'tests', lalu naik satu level ke root project
curr_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.abspath(os.path.join(curr_dir, '..'))

# Masukkan root project ke system path agar 'src' terbaca
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# --- 2. BARU IMPORT MODULE LAIN ---
import pytest
import subprocess
import allure
from datetime import datetime

# Sekarang import ini aman karena path sudah didaftarkan
from src.drivers.base_driver import init_driver

# Buat folder screenshots jika belum ada
os.makedirs("screenshots", exist_ok=True)

@pytest.fixture(scope="function")
def driver():
    drv = init_driver()
    yield drv
    drv.quit()

# Hook Screenshot & Allure Attachment
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        drv = item.funcargs.get("driver")
        if drv:
            ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            
            # 1. Simpan ke lokal
            filename = f"FAIL_{item.name}_{ts}.png"
            path = os.path.join("screenshots", filename)
            try:
                drv.save_screenshot(path)
                print(f"\n[screenshot] Saved locally: {path}")
            except Exception as e:
                print(f"[screenshot] Gagal save lokal: {e}")

            # 2. Attach ke Allure Report
            try:
                allure.attach(
                    drv.get_screenshot_as_png(),
                    name=f"Screenshot Fail - {ts}",
                    attachment_type=allure.attachment_type.PNG
                )
                print("[screenshot] Attached to Allure Report")
            except Exception as e:
                print(f"[screenshot] Gagal attach ke Allure: {e}")

# Hook Auto-Open Allure Report
def pytest_sessionfinish(session, exitstatus):
    allure_report_dir = "reports/allure-results"

    print(f"\n{'='*40}")
    print(f"[INFO] Sesi Test Selesai. Exit Code: {exitstatus}")

    if exitstatus == 0:
        print("[INFO] ✅ Semua Test PASSED!")
        print("[INFO] Membuka Allure Report otomatis...")
        try:
            subprocess.run(f"allure serve {allure_report_dir}", shell=True)
        except Exception as e:
            print(f"[ERROR] Gagal membuka Allure: {e}")
    else:
        print("[INFO] ❌ Ada Test yang FAILED.")
        print(f"[INFO] Report tidak dibuka otomatis. Cek terminal.")
    print(f"{'='*40}")