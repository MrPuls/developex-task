from selenium import webdriver
import src.page as page
from webdriver_manager.chrome import ChromeDriverManager


class UserRegistration:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get('http://localhost')

    def open_login_page(self):
        main_page = page.MainPage(self.driver)
        main_page.click_my_account_button()
        main_page.click_login_button()

    def login_or_create_user(self):
        login_page = page.LoginPage(self.driver)
        register_page = page.RegistrationPage(self.driver)
        login_page.login_user()
        if self.driver.current_url != 'https://localhost/index.php?route=account/account':
            login_page.create_new_user_button_click()
            register_page.register_new_user()
            register_page.logout_user()
            self.open_login_page()
            login_page.login_user()
            assert self.driver.current_url == 'https://localhost/index.php?route=account/account', \
                f'Login page was not accessed'


test = UserRegistration()
test.open_login_page()
test.login_or_create_user()