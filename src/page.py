import time
import selenium.common
from src.locators import MainPageLocators, RegistrationPageLocators, RegistrationSuccessLocators, \
    LoginPageLocators, MyAccountPageLocators, FeaturedListLocators, AppleCinemaLocators, CanonLocators, \
    OrderCheckoutLocators, PurchaseConfirmationLocators, PurchaseReturnLocators
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
        time.sleep(1)
        self.driver.find_element(*AppleCinemaLocators.SELECTOR_OPTION_BLUE).click()

    def _fill_textarea(self):
        self.driver.find_element(*AppleCinemaLocators.TEXTAREA).send_keys('test')

    def _upload_file(self):
        self.driver.execute_script('document.getElementById("input-option222").'
                                   'value="9ebb97b07a7020bb0d8fe37a61e213674e388000"')

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
        time.sleep(2)
        self.driver.find_element(*CanonLocators.SELECTOR).click()
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
        self.driver.find_element(*OrderCheckoutLocators.CHECKOUT_BTN).click()

    def _set_email(self):
        self.driver.find_element(*OrderCheckoutLocators.EMAIL).send_keys(dto.register_page_dto['EMAIL'])

    def _set_password(self):
        self.driver.find_element(*OrderCheckoutLocators.PASSWORD).send_keys(dto.register_page_dto['PASSWORD'])

    def _login(self):
        self.driver.find_element(*OrderCheckoutLocators.LOGIN_BTN).click()

    def set_new_delivery_data(self):
        try:
            self.driver.find_element(*OrderCheckoutLocators.NEW_ADDRESS_CHECKBOX).click()
        except selenium.common.exceptions.NoSuchElementException:
            pass

    def _set_first_name(self):
        self.driver.find_element(*OrderCheckoutLocators.FIRST_NAME).send_keys(dto.register_page_dto['FIRST_NAME'])

    def _set_last_name(self):
        self.driver.find_element(*OrderCheckoutLocators.LAST_NAME).send_keys(dto.register_page_dto['LAST_NAME'])

    def _set_address(self):
        self.driver.find_element(*OrderCheckoutLocators.ADDRESS).send_keys(dto.register_page_dto['ADDRESS'])

    def _set_city(self):
        self.driver.find_element(*OrderCheckoutLocators.CITY).send_keys(dto.register_page_dto['CITY'])

    def _set_post_code(self):
        self.driver.find_element(*OrderCheckoutLocators.POST_CODE).send_keys(dto.register_page_dto['POST_CODE'])

    def _set_region(self):
        self.driver.find_element(*OrderCheckoutLocators.REGION_SELECT).click()
        self.driver.find_element(*OrderCheckoutLocators.REGION_SELECT_OPTION).click()

    def _set_billing(self):
        self.driver.find_element(*OrderCheckoutLocators.BILLING_CONTINUE_BTN).click()

    def _set_delivery(self):
        self.driver.find_element(*OrderCheckoutLocators.DELIVERY_CONTINUE_BTN).click()

    def _set_delivery_method(self):
        self.driver.find_element(*OrderCheckoutLocators.DELIVERY_METHOD_CONTINUE_BTN).click()

    def _set_delivery_payment(self):
        self.driver.find_element(*OrderCheckoutLocators.PAYMENT_METHOD_TERMS_CHECKBOX).click()
        time.sleep(2)
        self.driver.find_element(*OrderCheckoutLocators.DELIVERY_PAYMENT_CONTINUE_BTN).click()

    def _set_payment_method(self):
        self.driver.find_element(*OrderCheckoutLocators.CONFIRM_ORDER_CONTINUE_BTN).click()

    def _click_order_placed_btn(self):
        self.driver.find_element(*OrderCheckoutLocators.ORDER_PLACED_CONTINUE_BTN).click()

    def checkout_purchase(self):
        time.sleep(2)
        self._click_cart_button()
        time.sleep(2)
        self._click_checkout_button()
        time.sleep(2)
        self._set_email()
        self._set_password()
        self._login()
        time.sleep(2)
        self.set_new_delivery_data()
        time.sleep(2)
        self._set_first_name()
        self._set_last_name()
        self._set_address()
        self._set_city()
        self._set_post_code()
        self._set_region()
        time.sleep(2)
        self._set_billing()
        time.sleep(2)
        self._set_delivery()
        time.sleep(2)
        self._set_delivery_method()
        time.sleep(2)
        self._set_delivery_payment()
        time.sleep(2)
        self._set_payment_method()
        time.sleep(2)
        self._click_order_placed_btn()
        assert self.driver.current_url == 'http://localhost/index.php?route=common/home', \
            f'Invalid url after purhase checkout. Expected [http://localhost/index.php?route=common/home] ' \
            f'Got: {self.driver.current_url}'


class CheckPurchaseStatus(BasePage):
    def open_account_menu(self):
        self.driver.find_element(*PurchaseConfirmationLocators.ACCOUNT_DROPDOWN_BTN).click()

    def open_order_history_tab(self):
        self.driver.find_element(*PurchaseConfirmationLocators.ORDER_HISTORY_BTN).click()

    def get_purchase_status(self):
        return self.driver.find_element(*PurchaseConfirmationLocators.ORDER_STATUS_TAB).text

    def check_order_history_status(self):
        time.sleep(1)
        self.open_account_menu()
        time.sleep(1)
        self.open_order_history_tab()
        time.sleep(1)
        assert self.get_purchase_status() == 'Pending', f'Invalid purchase status. Expected: Pending, ' \
                                                        f'Got: {self.get_purchase_status()}'


class CreateReturnRequest(BasePage):
    def _open_order_history(self):
        CheckPurchaseStatus(self.driver).open_account_menu()
        CheckPurchaseStatus(self.driver).open_order_history_tab()

    def _open_order_details(self):
        self.driver.find_element(*PurchaseReturnLocators.ORDER_DETAIL_BTN).click()

    def _choose_order_return_option(self):
        self.driver.find_element(*PurchaseReturnLocators.ORDER_RETURN_BTN).click()

    def _set_return_cause(self):
        self.driver.find_element(*PurchaseReturnLocators.RETURN_CAUSE_CHECKBOX).click()

    def _submit_return_request(self):
        self.driver.find_element(*PurchaseReturnLocators.SUBMIT_BTN).click()

    def _open_return_table(self):
        self.driver.find_element(*PurchaseReturnLocators.RETURNS_BTN).click()

    def _get_return_status(self):
        return self.driver.find_element(*PurchaseReturnLocators.RETURNS_INFO).text

    def make_return_and_verify_status(self):
        self._open_order_history()
        time.sleep(1)
        self._open_order_details()
        time.sleep(1)
        self._choose_order_return_option()
        time.sleep(1)
        self._set_return_cause()
        time.sleep(1)
        self._submit_return_request()
        time.sleep(1)
        self._open_return_table()

        assert self._get_return_status() == 'Awaiting Products', \
            f'Invalid Return status. Expected: Awaiting Products, Got: {self._get_return_status()}'
