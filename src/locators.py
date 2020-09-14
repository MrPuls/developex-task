from selenium.webdriver.common.by import By


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
