import pytest
import logging
from pages.openpayment_page import PaymentTunai, PaymentDebit, PaymentCredit, PaymentQRIS

#setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@pytest.mark.usefixtures('driver')
@pytest.mark.run(order=5)
# def test_payment_tunai(driver):
#     tunai = PaymentTunai(driver)
#     try:
#         logging.info('Mulai pengujian pembayaran tunai')
#         tunai.click_menu_openpayment()
#         tunai.input_amount()
#         tunai.click_button_lanjutkan()
#         tunai.scroll_to_text('TUNAI')
#         tunai.button_bayar_payment()
#         tunai.button_confirm_payment_tunai()
#         tunai.button_bayar_tunai()
#         tunai.success_page()
#         tunai.reprint_struk()
#         tunai.button_back()
#         tunai.openpayment_page()
#         logging.info("Pembayaran tunai berhasil")
#     except Exception as e :
#         logging.error(f'Terdapat error selama pengujian yaitu: {e}')
#         pytest.fail(f'terdapat error selama pengujian yaitu: {e}')

# def test_payment_debit(driver):
#     debit = PaymentDebit(driver)
#     try:
#         logging.info('Mulai pengujian pembayaran debit')
#         debit.click_menu_openpayment()
#         debit.input_amount()
#         debit.click_button_lanjutkan()
#         debit.scroll_to_text('DEBIT CARD')
#         debit.button_bayar_payment()
#         debit.button_confirm_payment_debit()
#         debit.insert_card_page()
#         debit.confirm_payment_debit()
#         debit.input_PIN_debit()
#         debit.success_page()
#         debit.reprint_struk()
#         debit.button_back()
#         debit.openpayment_page()
#         logging.info("Pembayaran debit berhasil")
#     except Exception as e :
#         logging.error(f'Terdapat error selama pengujian yaitu: {e}')
#         pytest.fail(f'terdapat error selama pengujian yaitu: {e}')

# def test_payment_credit(driver):
#     credit = PaymentCredit(driver)
#     try:
#         logging.info('Mulai pengujian pembayaran credit')
#         credit.click_menu_openpayment()
#         credit.input_amount()
#         credit.click_button_lanjutkan()
#         credit.scroll_to_text("CREDIT CARD")
#         credit.button_bayar_payment()
#         credit.button_confirm_payment_credit()
#         credit.insert_card_page()
#         credit.confirm_payment_credit()
#         credit.input_PIN_credit()
#         credit.success_page()
#         credit.reprint_struk()
#         credit.button_back()
#         credit.openpayment_page()
#         logging.info("Pembayaran credit berhasil")
#     except Exception as e :
#         logging.error(f'Terdapat error selama pengujian yaitu: {e}')
#         pytest.fail(f'terdapat error selama pengujian yaitu: {e}')

def test_payment_QRIS(driver):
    QRIS = PaymentQRIS(driver)
    try:
        logging.info('Mulai pengujian pembayaran QRIS')
        QRIS.click_menu_openpayment()
        QRIS.input_amount()
        QRIS.click_button_lanjutkan()
        QRIS.swipe_by_coordinates(300, 1000, 350, 250)
        QRIS.select_payment("QRIS")
        QRIS.button_bayar_payment()
        QRIS.button_confirm_payment_QRIS()
        QRIS.wait_for_qrcode()
        QRIS.qris_page()
        QRIS.success_page()
        QRIS.reprint_struk()
        QRIS.button_back()
        QRIS.openpayment_page()
        logging.info("Pembayaran QRIS berhasil")
    except Exception as e :
        logging.error(f'Terdapat error selama pengujian yaitu: {e}')
        pytest.fail(f'terdapat error selama pengujian yaitu: {e}')


