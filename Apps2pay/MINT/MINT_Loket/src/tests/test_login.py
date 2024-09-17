import unittest
from src.pages.login_page import LoginPage
from conftest import driver

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = driver()
        cls.login_page = LoginPage(cls.driver)
    
    @classmethod
    def tearDownClass(cls):
        # Hentikan driver setelah pengujian
        cls.driver.quit()

    def test_login_success(self):
        try:
            # Langkah pengujian
            self.login_page.click_next_button()
            self.login_page.set_cid('00109')
            self.login_page.set_username('kevintesting')
            self.login_page.set_password('999999')
            self.login_page.click_login_button()
            self.login_page.wait_for_home_page()

            print('Login berhasil')
        except Exception as e:
            self.fail(f'terdapat error selama pengujian yaitu: {e}')
        
if __name__ == '__main__':
    unittest.main()
