from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PosKasir:
    def __init__(self, driver):
        self.driver = driver
    
    def click_menu_poskasir(self):
        button_poskasir = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.mkpmobile.retail.mitramint:id/lnProdukBiller").instance(0)')))
        button_poskasir.click()

    def poskasir_page(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/action_bar_root')))

    def search_product(self, product):
        search_product_poskasir = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/searchProduct')))
        search_product_poskasir.send_keys(product)

    def button_add_product(self):
        add_product_poskasir = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Tambah")')))
        add_product_poskasir.click()

    def button_checkout_product(self):
        checkout_product_poskasir = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("CHECKOUT")')))
        checkout_product_poskasir.click()

    def button_add_discount(self):
        add_discount_product = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Tambah diskon")')))
        add_discount_product.click()

    def add_nominal_discount(self, nominal):
        input_nominal = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/edInputDiscon')))
        input_nominal.send_keys(nominal)

    def button_confirm_discount(self):
        click_confirm_discount = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Terapkan harga")')))
        click_confirm_discount.click()

    def button_note_product(self):
        click_add_note_product = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnCatatan')))
        click_add_note_product.click()

    def add_note_product(self, note):
        input_note = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/edit_text')))
        input_note.send_keys(note)

    def button_save_note(self):
        click_save_note = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/saveButton')))
        click_save_note.click()

    def click_next_checkout(self):
        click_button_next = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnCkeckout')))
        click_button_next.click()

    def scroll_to_text(self, text):
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

class PaymentTunai(PosKasir):
    def __init__(self, driver):
        super().__init__(driver)
    
    def button_confirm_payment_tunai(self):
        click_button_confirm_payment_tunai = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnLanjutTr')))
        click_button_confirm_payment_tunai.click()

    def button_bayar_tunai(self):
        button_bayar_tunai = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnBayarTunai')))
        button_bayar_tunai.click()

class PaymentDebit(PosKasir): 
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

class PaymentCredit(PosKasir):
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

class PaymentQRIS(PosKasir):
    def __init__(self, driver):
        super().__init__(driver)
    
    def button_confirm_payment_QRIS(self):
        click_button_confirm_payment_QRIS = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/lnLanjutTr')))
        click_button_confirm_payment_QRIS.click()
    
    def wait_for_qrcode(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((AppiumBy.ID, 'com.mkpmobile.retail.mitramint:id/linMainBg')))
        