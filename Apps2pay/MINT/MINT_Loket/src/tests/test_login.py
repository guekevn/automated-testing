import pytest
import logging
from pages.login_page import LoginPage

#setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures("driver")
@pytest.mark.run(order=1)
def test_login_success(driver):
        login_page=LoginPage(driver)
        try:
            logging.info('Mulai pengujian login')
            login_page.click_next_button()
            login_page.set_cid('00109')
            login_page.set_username('kevintesting')
            login_page.set_password('999999')
            login_page.click_login_button()
            login_page.wait_for_home_page()
            logging.info('Login berhasil')
        except Exception as e:
            logging.error(f'Terdapat error selama pengujian yaitu: {e}')
            pytest.fail(f'terdapat error selama pengujian yaitu: {e}')
