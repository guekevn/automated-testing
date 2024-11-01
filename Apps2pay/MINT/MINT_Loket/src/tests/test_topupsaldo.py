import pytest
import logging
from pages.topupsaldo_page import TopUpSaldoPage

#setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures("driver")
@pytest.mark.run(order=3)
def test_topupsaldo_success(driver):
    topupsaldo = TopUpSaldoPage(driver)
    try:
        logging.info('Mulai pengujian topup saldo')
        topupsaldo.click_menu_topupsaldo()
        topupsaldo.method_payment()
        topupsaldo.QRIS_payment()
        topupsaldo.click_pilih_list_payment()
        topupsaldo.input_nominal()
        topupsaldo.click_button_lanjut()
        topupsaldo.click_button_lanjut_inquiry()
        topupsaldo.wait_for_qris()
        topupsaldo.wait_for_payment_success()
        topupsaldo.click_button_print_struk()
        topupsaldo.click_button_back()
        topupsaldo.click_button_back_home()
        topupsaldo.wait_for_home_page()
        logging.info('Topup saldo berhasil')
    except Exception as e:
        logging.error(f'Terdapat error selama pengujian yaitu: {e}')
        pytest.fail(f'terdapat error selama pengujian yaitu: {e}')
