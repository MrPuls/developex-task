from selenium import webdriver
import src.page as page
from webdriver_manager.chrome import ChromeDriverManager


class SetUp:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('http://localhost')


class UserRegistration(SetUp):

    def _open_login_page(self):
        main_page = page.MainPage(self.driver)
        main_page.click_my_account_button()
        main_page.click_login_button()

    def _login_or_create_user(self):
        login_page = page.LoginPage(self.driver)
        register_page = page.RegistrationPage(self.driver)
        login_page.login_user()
        if self.driver.current_url != 'https://localhost/index.php?route=account/account':
            login_page.create_new_user_button_click()
            register_page.register_new_user()
            register_page.logout_user()
            self._open_login_page()
            login_page.login_user()
            assert self.driver.current_url == 'https://localhost/index.php?route=account/account', \
                f'Login page was not accessed'

    def create_user(self):
        self._open_login_page()
        self._login_or_create_user()


class MakePurchase(SetUp):

    def add_items_to_cart(self):
        page.MainPage(self.driver).add_item_to_cart()

    def checkout_items(self):
        page.FillOrderCheckoutInfo(self.driver).checkout_purchase()

    def check_order_history(self):
        page.CheckPurchaseStatus(self.driver).check_order_history_status()


class CreateReturnRequest(SetUp):
    def create_return_request_and_verify_status(self):
        page.CreateReturnRequest(self.driver).make_return_and_verify_status()
