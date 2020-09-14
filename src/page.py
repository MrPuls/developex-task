from src.locators import MainPageLocators, RegistrationPageLocators, RegistrationSuccessLocators, \
    LoginPageLocators, MyAccountPageLocators
import src.tests_dto as dto


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    def click_my_account_button(self):
        my_account_btn = self.driver.find_element(*MainPageLocators.MY_ACCOUNT_BTN)
        my_account_btn.click()

    def click_login_button(self):
        register_btn = self.driver.find_element(*MainPageLocators.LOGIN_BTN)
        register_btn.click()


class LoginPage(BasePage):
    def login_user(self):
        self.driver.find_element(*LoginPageLocators.EMAIL).send_keys(dto.register_page_dto['EMAIL'])
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(dto.register_page_dto['PASSWORD'])
        self.driver.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def create_new_user_button_click(self):
        self.driver.find_element(*LoginPageLocators.NEW_CUSTOMER_BTN).click()


class RegistrationPage(BasePage):

    def fill_registration_info(self):
        self.driver.find_element(*RegistrationPageLocators.FIRST_NAME).send_keys(dto.register_page_dto['FIRST_NAME'])

        self.driver.find_element(*RegistrationPageLocators.LAST_NAME).send_keys(dto.register_page_dto['LAST_NAME'])

        self.driver.find_element(*RegistrationPageLocators.EMAIL).send_keys(dto.register_page_dto['EMAIL'])

        self.driver.find_element(*RegistrationPageLocators.PHONE_NUMBER).\
            send_keys(dto.register_page_dto['PHONE_NUMBER'])

        self.driver.find_element(*RegistrationPageLocators.PASSWORD).send_keys(dto.register_page_dto['PASSWORD'])

        self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD).\
            send_keys(dto.register_page_dto['PASSWORD'])

        self.driver.find_element(*RegistrationPageLocators.SUBSCRIPTION).click()

        self.driver.find_element(*RegistrationPageLocators.PRIVACY_POLICY).click()

    def click_register_user_continue_button(self):
        continue_btn = self.driver.find_element(*RegistrationPageLocators.CONTINUE)
        continue_btn.click()

    def user_created_continue_button_click(self):
        self.driver.find_element(*RegistrationSuccessLocators.CONTINUE).click()

    def logout_user(self):
        self.driver.find_element(*MyAccountPageLocators.LOGOUT).click()
        self.driver.find_element(*MyAccountPageLocators.CONTINUE).click()

    def register_new_user(self):
        self.fill_registration_info()
        self.click_register_user_continue_button()
        self.user_created_continue_button_click()

