from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    FIRST_ITEM_DESCRIPTION = (By.XPATH, "//td[3]")

    def verify_first_item_description_match(self, expected_description):
        assert self.find(self.FIRST_ITEM_DESCRIPTION).text == expected_description
