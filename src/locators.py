from selenium.webdriver.common.by import By
import random


class MainPageLocators(object):
    MY_ACCOUNT_BTN = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')
    LOGIN_BTN = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')


class RegistrationPageLocators(object):
    FIRST_NAME = (By.ID, 'input-firstname')
    LAST_NAME = (By.ID, 'input-lastname')
    EMAIL = (By.ID, 'input-email')
    PHONE_NUMBER = (By.ID, 'input-telephone')
    PASSWORD = (By.ID, 'input-password')
    CONFIRM_PASSWORD = (By.ID, 'input-confirm')
    SUBSCRIPTION = (By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/label[2]/input')
    PRIVACY_POLICY = (By.XPATH, '//*[@id="content"]/form/div/div/input[1]')
    CONTINUE = (By.XPATH, '//*[@id="content"]/form/div/div/input[2]')


class RegistrationSuccessLocators(object):
    CONTINUE = (By.XPATH, '//*[@id="content"]/div/div/a')


class LoginPageLocators(object):
    EMAIL = (By.ID, 'input-email')
    PASSWORD = (By.ID, 'input-password')
    LOGIN_BTN = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
    NEW_CUSTOMER_BTN = (By.XPATH, '//*[@id="content"]/div/div[1]/div/a')


class MyAccountPageLocators(object):
    LOGOUT = (By.XPATH, '//*[@id="column-right"]/div/a[13]')
    LOGOUT_CONTINUE_BTN = (By.XPATH, '//*[@id="content"]/div/div/a')
    CONTINUE = (By.XPATH, '//*[@id="content"]/div/div/a')


class FeaturedListLocators(object):
    item_1 = random.randint(1, 4)
    item_2 = random.randint(1, 4)
    ADD_FIRST_ITEM_TO_CART_BTN = (By.XPATH,
                                  f'//*[@id="content"]/div[2]/div[{item_1}]/div/div[3]/button[1]')
    ADD_SECOND_ITEM_TO_CART_BTN = (By.XPATH,
                                   f'//*[@id="content"]/div[2]/div[{item_2}]/div/div[3]/button[1]')


class AppleCinemaLocators(object):
    RADIO = (By.CSS_SELECTOR, '#input-option218 > div:nth-child(1) > label > input[type=radio]')
    CHECKBOX = (By.XPATH, '//*[@id="input-option223"]/div[2]/label/input')
    TEXT = (By.XPATH, '//*[@id="input-option208"]')
    SELECTOR = (By.XPATH, '//*[@id="input-option217"]')
    SELECTOR_OPTION_BLUE = (By.CSS_SELECTOR, '#input-option217 > option:nth-child(3)')
    TEXTAREA = (By.XPATH, '//*[@id="input-option209"]')
    FILE = (By.XPATH, '//*[@id="button-upload222"]')
    ADD_TO_CART_BTN = (By.XPATH, '//*[@id="button-cart"]')


class CanonLocators:
    SELECTOR = (By.XPATH, '//*[@id="input-option226"]')
    SELECTOR_OPTION_BLUE = (By.CSS_SELECTOR, '#input-option226 > option:nth-child(3)')
    ADD_TO_CART_BTN = (By.XPATH, '//*[@id="button-cart"]')


class OrderCheckoutLocators:
    CART_BTN = (By.XPATH, '//*[@id="cart"]/button')
    CHECKOUT_BTN = (By.XPATH, '//*[@id="cart"]/ul/li[2]/div/p/a[2]')
    EMAIL = (By.XPATH, '//*[@id="input-email"]')
    PASSWORD = (By.XPATH, '//*[@id="input-password"]')
    LOGIN_BTN = (By.XPATH, '//*[@id="button-login"]')
    NEW_ADDRESS_CHECKBOX = (By.CSS_SELECTOR,
                            '#collapse-payment-address > div > form > div:nth-child(3) > label > input[type=radio]')
    FIRST_NAME = (By.XPATH, '//*[@id="input-payment-firstname"]')
    LAST_NAME = (By.XPATH, '//*[@id="input-payment-lastname"]')
    ADDRESS = (By.XPATH, '//*[@id="input-payment-address-1"]')
    CITY = (By.XPATH, '//*[@id="input-payment-city"]')
    POST_CODE = (By.XPATH, '//*[@id="input-payment-postcode"]')
    REGION_SELECT = (By.XPATH, '//*[@id="input-payment-zone"]')
    REGION_SELECT_OPTION = (By.XPATH, '//*[@id="input-payment-zone"]/option[7]')
    BILLING_CONTINUE_BTN = (By.XPATH, '//*[@id="button-payment-address"]')
    DELIVERY_CONTINUE_BTN = (By.XPATH, '//*[@id="button-shipping-address"]')
    DELIVERY_METHOD_CONTINUE_BTN = (By.XPATH, '//*[@id="button-shipping-method"]')
    DELIVERY_PAYMENT_CONTINUE_BTN = (By.XPATH, '//*[@id="button-payment-method"]')
    PAYMENT_METHOD_TERMS_CHECKBOX = (By.CSS_SELECTOR,
                                     '#collapse-payment-method > div > div.buttons > div > input[type=checkbox]:'
                                     'nth-child(2)')
    CONFIRM_ORDER_CONTINUE_BTN = (By.XPATH, '//*[@id="button-confirm"]')
    ORDER_PLACED_CONTINUE_BTN = (By.XPATH, '//*[@id="content"]/div/div/a')


class PurchaseConfirmationLocators:
    ACCOUNT_DROPDOWN_BTN = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/a')
    ORDER_HISTORY_BTN = (By.XPATH, '//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')
    ORDER_HISTORY_HEADERS = (By.XPATH, '//*[@id="content"]/div[1]/table/thead/tr')
    ORDER_HISTORY_BODY = (By.XPATH, '//*[@id="content"]/div[1]/table/tbody/tr')
    ORDER_STATUS_TAB = (By.XPATH, '//*[@id="content"]/div[1]/table/tbody/tr/td[4]')


class PurchaseReturnLocators:
    order_history_table_size = len((By.XPATH, '//*[@id="content"]/div[1]/table/tbody'))
    order_detail_table_size = len((By.XPATH, '//*[@id="content"]/div[1]/table/tbody'))

    '//*[@id="content"]/form/fieldset[2]/div[4]/div/div[1]/label/input'
    '//*[@id="content"]/form/fieldset[2]/div[4]/div/div[4]/label/input'

    ORDER_DETAIL_BTN = \
        (By.XPATH, f'//*[@id="content"]/div[1]/table/tbody/tr[{random.randint(1, order_history_table_size)}]/td[7]/a')
    ORDER_RETURN_BTN = \
        (By.XPATH, f'//*[@id="content"]/div[1]/table/tbody/tr[{random.randint(1, order_detail_table_size)}]/td[6]/a[2]')
    RETURN_CAUSE_CHECKBOX = \
        (By.CSS_SELECTOR,
         '#content > form > fieldset:nth-child(2) > div:nth-child(5) > '
         'div > div:nth-child(1) > label > input[type=radio]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="content"]/form/div/div[2]/input')
    RETURNS_BTN = (By.XPATH, '//*[@id="column-right"]/div/a[10]')
    RETURNS_INFO = (By.XPATH, '//*[@id="content"]/div[1]/table/tbody/tr[3]/td[2]')
