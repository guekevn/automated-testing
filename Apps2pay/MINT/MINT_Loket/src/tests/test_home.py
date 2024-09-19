import pytest
import logging
from pages.home_page import HomePage

#setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures("driver")
@pytest.mark.run(order=2)
def test_homepage(driver):
        home_page = HomePage(driver)
        try:
            logging.info('Mulai menampilkan homepage')
            home_page.click_hide_button()
            home_page.wait_for_homepage()
            logging.info('Berhasil menampilkan homepage')
        except Exception as e:
            logging.error(f'Terdapat error selama pengujian yaitu: {e}')
            pytest.fail(f'terdapat error selama pengujian yaitu: {e}')
        