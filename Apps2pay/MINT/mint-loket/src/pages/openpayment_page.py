from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
import time

class OpenPayment:
    def __init__ (self, driver):
        self.driver = driver

    def click_menu_openpayment(self):
        button_openpayment = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.mkpmobile.retail.mitramint:id/lnProdukBiller").instance(1)')))
        button_openpayment.click()

    def openpayment_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/action_bar_root')))
    
    def input_amount(self):
        input_amount = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/edNominalEdc')))
        input_amount.send_keys('100')

    def click_button_lanjutkan(self):
        button_lanjutkan = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnKonfirmEdc')))
        button_lanjutkan.click()
        time.sleep(2)

    def swipe_by_coordinates(self, start_x, start_y, end_x, end_y):
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=800)

    def select_payment(self, text):
        button_pilih_payment = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollTextIntoView("'+ text +'")')))
        button_pilih_payment.click()

    def button_bayar_payment(self):
        click_button_bayar = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/tombolPayment')))
        click_button_bayar.click()

    def success_page(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/action_bar_root')))

    def reprint_struk(self):
        button_reprint_struk = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/btnLanjut')))
        button_reprint_struk.click()

    def button_back(self):
        click_button_back = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/backHomeRetail')))
        click_button_back.click()

class PaymentTunai(OpenPayment):
    def __init__(self, driver):
        super().__init__(driver)
    
    def button_confirm_payment_tunai(self):
        click_button_confirm_payment_tunai = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnLanjutTr')))
        click_button_confirm_payment_tunai.click()

    def button_bayar_tunai(self):
        button_bayar_tunai = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnBayarTunai')))
        button_bayar_tunai.click()

class PaymentDebit(OpenPayment): 
    def __init__(self, driver):
        super().__init__(driver)

    def button_confirm_payment_debit(self):
        click_button_confirm_payment_debit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnLanjutTr')))
        click_button_confirm_payment_debit.click()

    def insert_card_page(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/layLoading2')))

    def confirm_payment_debit(self):
        click_confirm_payment_debit = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/btnLanjut')))
        click_confirm_payment_debit.click()
    
    def input_PIN_debit(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ID, 'com.whty.tysecuritypin:id/keyboard_view')))

class PaymentCredit(OpenPayment):
    def __init__(self, driver):
        super().__init__(driver)
    
    def button_confirm_payment_credit(self):
        click_button_confirm_payment_credit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnLanjutTr')))
        click_button_confirm_payment_credit.click()

    def insert_card_page(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/layLoading2')))

    def confirm_payment_credit(self):
        click_confirm_payment_credit = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/btnLanjut')))
        click_confirm_payment_credit.click()
    
    def input_PIN_credit(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ID, 'com.whty.tysecuritypin:id/keyboard_view')))

class PaymentQRIS(OpenPayment):
    def __init__(self, driver):
        super().__init__(driver)
    
    def button_confirm_payment_QRIS(self):
        click_button_confirm_payment_QRIS = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnLanjutTr')))
        click_button_confirm_payment_QRIS.click()
    
    def wait_for_qrcode(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/linMainBg')))

    def qris_page(self):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/layQris')))
        time.sleep(60)
        