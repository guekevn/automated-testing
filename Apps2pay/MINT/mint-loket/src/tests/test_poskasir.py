import pytest
import logging
from pages.poskasir_page import PaymentTunai, PaymentDebit, PaymentCredit, PaymentQRIS

#setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures('driver')
@pytest.mark.run(order=4)
def test_payment_tunai(driver):
    tunai = PaymentTunai(driver)
    try:
        logging.info('Mulai pengujian pembayaran tunai')
        tunai.click_menu_poskasir()
        tunai.search_product('Kopi')
        tunai.button_add_product()
        tunai.button_checkout_product()
        tunai.button_add_discount()
        tunai.add_nominal_discount('500')
        tunai.button_confirm_discount()
        tunai.button_note_product()
        tunai.add_note_product('less sugar')
        driver.back()
        tunai.button_save_note()
        tunai.click_next_checkout()
        tunai.scroll_to_text('TUNAI')
        tunai.button_bayar_payment()
        tunai.button_confirm_payment_tunai()
        tunai.button_bayar_tunai()
        tunai.success_page()
        tunai.reprint_struk()
        tunai.button_back()
        tunai.poskasir_page()
        logging.info("Pembayaran tunai berhasil")
    except Exception as e :
        logging.error(f'Terdapat error selama pengujian yaitu: {e}')
        pytest.fail(f'terdapat error selama pengujian yaitu: {e}')

def test_payment_debit(driver):
    debit = PaymentDebit(driver)
    try:
        logging.info('Mulai pengujian pembayaran debit')
        debit.search_product('Kopi')
        debit.button_add_product()
        debit.button_checkout_product()
        debit.click_next_checkout()
        debit.scroll_to_text('DEBIT CARD')
        debit.button_bayar_payment()
        debit.button_confirm_payment_debit()
        debit.insert_card_page()
        debit.confirm_payment_debit()
        debit.input_PIN_debit()
        debit.success_page()
        debit.reprint_struk()
        debit.button_back()
        debit.poskasir_page()
        logging.info("Pembayaran debit berhasil")
    except Exception as e :
        logging.error(f'Terdapat error selama pengujian yaitu: {e}')
        pytest.fail(f'terdapat error selama pengujian yaitu: {e}')

def test_payment_credit(driver):
    credit = PaymentCredit(driver)
    try:
        logging.info('Mulai pengujian pembayaran credit')
        credit.search_product('Kopi')
        credit.button_add_product()
        credit.button_checkout_product()
        credit.click_next_checkout()
        credit.scroll_to_text("CREDIT CARD")
        credit.button_bayar_payment()
        credit.button_confirm_payment_credit()
        credit.insert_card_page()
        credit.confirm_payment_credit()
        credit.input_PIN_credit()
        credit.success_page()
        credit.reprint_struk()
        credit.button_back()
        credit.poskasir_page()
        logging.info("Pembayaran credit berhasil")
    except Exception as e :
        logging.error(f'Terdapat error selama pengujian yaitu: {e}')
        pytest.fail(f'terdapat error selama pengujian yaitu: {e}')

def test_payment_QRIS(driver):
    QRIS = PaymentQRIS(driver)
    try:
        logging.info('Mulai pengujian pembayaran credit')
        QRIS.search_product('Kopi')
        QRIS.button_add_product()
        QRIS.button_checkout_product()
        QRIS.click_next_checkout()
        QRIS.scroll_to_text("QRIS")
        QRIS.button_bayar_payment()
        QRIS.button_confirm_payment_QRIS()
        QRIS.wait_for_qrcode()
        QRIS.success_page()
        QRIS.reprint_struk()
        QRIS.button_back()
        QRIS.poskasir_page()
        logging.info("Pembayaran credit berhasil")
    except Exception as e :
        logging.error(f'Terdapat error selama pengujian yaitu: {e}')
        pytest.fail(f'terdapat error selama pengujian yaitu: {e}')


