from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    ANGELFISH = (By.XPATH, "//td[text()='Angelfish']/preceding-sibling::td/a")
    LARGE_ANGELFISH = (By.XPATH, "//td[contains(text(), 'Large')]/preceding::td/a")
    LARGE_ANGELFISH_ADD_TO_CART = \
        (By.XPATH, "//td[a[contains(text(),'EST-1')]]/following-sibling::td/a[contains(text(),'Add to Cart')]")

    def click_angelfish(self):
        self.find(self.ANGELFISH).click()

    def click_large_angelfish(self):
        self.find(self.LARGE_ANGELFISH).click()

    def click_large_angelfish_add_to_cart(self):
        self.find(self.LARGE_ANGELFISH_ADD_TO_CART).click()