from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class NewAccountPage(BasePage):
    FORM_USERNAME = (By.NAME, "username")
    FORM_PASSWORD = (By.NAME, "password")
    FORM_REPEATED_PASSWORD = (By.NAME, "repeatedPassword")

    FORM_FIRST_NAME = (By.NAME, "account.firstName")
    FORM_LAST_NAME = (By.NAME, "account.lastName")
    FORM_EMAIL = (By.NAME, "account.email")
    FORM_PHONE = (By.NAME, "account.phone")

    FORM_ADDRESS1 = (By.NAME, "account.address1")
    FORM_ADDRESS2 = (By.NAME, "account.address2")
    FORM_CITY = (By.NAME, "account.city")
    FORM_STATE = (By.NAME, "account.state")
    FORM_ZIP = (By.NAME, "account.zip")
    FORM_COUNTRY = (By.NAME, "account.country")

    REGISTER_BTN = (By.NAME, "newAccount")

    def enter_username(self, username):
        self.find(self.FORM_USERNAME).send_keys(username)

    def enter_password(self, password):
        self.find(self.FORM_PASSWORD).send_keys(password)
        self.find(self.FORM_REPEATED_PASSWORD).send_keys(password)

    def enter_account_data(self, first_name, last_name, email, phone):
        self.find(self.FORM_FIRST_NAME).send_keys(first_name)
        self.find(self.FORM_LAST_NAME).send_keys(last_name)
        self.find(self.FORM_EMAIL).send_keys(email)
        self.find(self.FORM_PHONE).send_keys(phone)

    def enter_address_data(self, address1, address2, city, state, zip, country):
        self.find(self.FORM_ADDRESS1).send_keys(address1)
        self.find(self.FORM_ADDRESS2).send_keys(address2)
        self.find(self.FORM_CITY).send_keys(city)
        self.find(self.FORM_STATE).send_keys(state)
        self.find(self.FORM_ZIP).send_keys(zip)
        self.find(self.FORM_COUNTRY).send_keys(country)

    def click_register(self):
        self.find(self.REGISTER_BTN).click()