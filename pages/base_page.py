from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    SIGN_IN = (By.LINK_TEXT, "Sign In")
    SIGN_OUT = (By.LINK_TEXT, "Sign Out")
    MY_ACCOUNT = (By.LINK_TEXT, "My Account")

    def __init__(self, driver):
        self.driver = driver
        self._wait = WebDriverWait(driver, 5)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    def wait_for(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    def click_sign_in(self):
        self.find(self.SIGN_IN).click()

    def click_sign_out(self):
        self.find(self.SIGN_OUT).click()

    def click_my_account(self):
        self.find(self.MY_ACCOUNT).click()

    def wait_my_account(self):
        return self.wait_for(self.MY_ACCOUNT)

    def is_sign_in_visible(self):
        return self.find(self.SIGN_IN).is_displayed()

    def is_my_account_visible(self):
        return self.wait_my_account().is_displayed()