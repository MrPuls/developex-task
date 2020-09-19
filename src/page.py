import time
from src.locators import MainPageLocators, RegistrationPageLocators, RegistrationSuccessLocators, \
    LoginPageLocators, MyAccountPageLocators, FeaturedListLocators, AppleCinemaLocators, CanonLocators, \
    OrderCheckoutLocators, PurchaseConfirmationLocators
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

    def add_item_to_cart(self):
        self.driver.find_element(*FeaturedListLocators.ADD_FIRST_ITEM_TO_CART_BTN).click()
        self.driver.find_element(*FeaturedListLocators.ADD_SECOND_ITEM_TO_CART_BTN).click()
        FillAppleCinemaInfo(self.driver).fill_full_info()
        FillCanonInfo(self.driver).fill_full_info()


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

        self.driver.find_element(*RegistrationPageLocators.PHONE_NUMBER). \
            send_keys(dto.register_page_dto['PHONE_NUMBER'])

        self.driver.find_element(*RegistrationPageLocators.PASSWORD).send_keys(dto.register_page_dto['PASSWORD'])

        self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD). \
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


class FillAppleCinemaInfo(BasePage):
    def _check_radio(self):
        self.driver.find_element(*AppleCinemaLocators.RADIO).click()

    def _check_checkbox(self):
        self.driver.find_element(*AppleCinemaLocators.CHECKBOX).click()

    def _fill_text_field(self):
        self.driver.find_element(*AppleCinemaLocators.TEXT).send_keys('test')

    def _check_selector(self):
        self.driver.find_element(*AppleCinemaLocators.SELECTOR).click()
        time.sleep(2)
        self.driver.find_element(*AppleCinemaLocators.SELECTOR_OPTION_BLUE).click()

    def _fill_textarea(self):
        self.driver.find_element(*AppleCinemaLocators.TEXTAREA).send_keys('test')

    def _upload_file(self):
        self.driver.execute_script('document.getElementById("input-option222").'
                                   'value="9ebb97b07a7020bb0d8fe37a61e213674e388000"')
        time.sleep(15)

    def _add_to_cart(self):
        self.driver.find_element(*AppleCinemaLocators.ADD_TO_CART_BTN).click()

    def fill_full_info(self):
        time.sleep(2)
        if self.driver.current_url == 'http://localhost/index.php?route=product/product&product_id=42':
            self._check_radio()
            self._check_checkbox()
            self._fill_text_field()
            self._check_selector()
            self._fill_textarea()
            self._fill_text_field()
            self._upload_file()
            self._add_to_cart()


class FillCanonInfo(BasePage):
    def _check_selector(self):
        self.driver.find_element(*CanonLocators.SELECTOR).click()
        time.sleep(2)
        self.driver.find_element(*CanonLocators.SELECTOR_OPTION_BLUE).click()

    def _add_to_cart(self):
        self.driver.find_element(*CanonLocators.ADD_TO_CART_BTN).click()

    def fill_full_info(self):
        time.sleep(2)
        if self.driver.current_url == 'http://localhost/index.php?route=product/product&product_id=30':
            self._check_selector()
            self._add_to_cart()


class FillOrderCheckoutInfo(BasePage):
    def _click_cart_button(self):
        self.driver.find_element(*OrderCheckoutLocators.CART_BTN).click()

    def _click_checkout_button(self):
        self.driver.find_element(*OrderCheckoutLocators.CHECKOUT_BTN)

    def _set_email(self):
        self.driver.find_element(*OrderCheckoutLocators.EMAIL)

    def _set_password(self):
        self.driver.find_element(*OrderCheckoutLocators.PASSWORD)

    def _login(self):
        self.driver.find_element(*OrderCheckoutLocators.LOGIN_BTN)

    def _set_first_name(self):
        self.driver.find_element(*OrderCheckoutLocators.FIRST_NAME)

    def _set_last_name(self):
        self.driver.find_element(*OrderCheckoutLocators.LAST_NAME)

    def _set_address(self):
        self.driver.find_element(*OrderCheckoutLocators.ADDRESS)

    def _set_city(self):
        self.driver.find_element(*OrderCheckoutLocators.CITY)

    def _set_post_code(self):
        self.driver.find_element(*OrderCheckoutLocators.POST_CODE)

    def _set_region(self):
        self.driver.find_element(*OrderCheckoutLocators.REGION_SELECT)
        self.driver.find_element(*OrderCheckoutLocators.REGION_SELECT_OPTION)

    def _set_billing(self):
        self.driver.find_element(*OrderCheckoutLocators.BILLING_CONTINUE_BTN)

    def _set_delivery(self):
        self.driver.find_element(*OrderCheckoutLocators.DELIVERY_CONTINUE_BTN)

    def _set_delivery_method(self):
        self.driver.find_element(*OrderCheckoutLocators.DELIVERY_METHOD_CONTINUE_BTN)

    def _set_delivery_payment(self):
        self.driver.find_element(*OrderCheckoutLocators.DELIVERY_PAYMENT_CONTINUE_BTN)

    def _set_payment_method(self):
        self.driver.find_element(*OrderCheckoutLocators.PAYMENT_METHOD_TERMS_CHECKBOX)
        self.driver.find_element(*OrderCheckoutLocators.CONFIRM_ORDER_CONTINUE_BTN)
