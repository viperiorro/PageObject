from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "a.Button")

    def click_add_to_cart(self):
        self.find(self.ADD_TO_CART_BUTTON).click()