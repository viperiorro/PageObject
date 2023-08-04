from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignInPage(BasePage):
    FORM_USERNAME = (By.NAME, "username")
    FORM_PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.NAME, "signon")
    REGISTER_NOW_BTN = (By.LINK_TEXT, "Register Now!")

    def enter_username(self, username):
        username_field = self.find(self.FORM_USERNAME)
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.find(self.FORM_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.find(self.LOGIN_BTN).click()

    def click_register_now(self):
        self.find(self.REGISTER_NOW_BTN).click()
