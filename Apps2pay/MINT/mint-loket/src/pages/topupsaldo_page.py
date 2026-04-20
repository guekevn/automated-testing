from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TopUpSaldoPage:
    def __init__(self, driver):
        self.driver = driver

    def click_menu_topupsaldo(self):
        topupsaldo_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/containerTopupSaldo')))
        topupsaldo_button.click()

    def method_payment(self):
        button_method_payment = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/bttnMethodPayment')))
        button_method_payment.click()

    def QRIS_payment(self):
        button_qris = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.mkpmobile.retail.mitramint:id/bgPayment"])[1]')))
        button_qris.click()

    def click_pilih_list_payment(self):
        button_pilih_payment = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/bttnLanjut')))
        button_pilih_payment.click()

    def input_nominal(self):
        input_nominal = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/bttn1')))
        input_nominal.click()

    def click_button_lanjut(self):
        button_lanjut = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/btnLanjut')))
        button_lanjut.click()

    def click_button_lanjut_inquiry(self):
        button_lanjut_inquiry = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/bttnLanjut')))
        button_lanjut_inquiry.click()

    def wait_for_qris(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/action_bar_root')))

    def wait_for_payment_success(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/action_bar_root')))

    def click_button_print_struk(self):
        button_print_struk = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/btnLanjut')))
        button_print_struk.click()

    def click_button_back(self):
        button_back = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/backHomeRetail')))
        button_back.click()

    def click_button_back_home(self):
        button_back = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/buttonBack')))
        button_back.click()

    def wait_for_home_page(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/action_bar_root')))
