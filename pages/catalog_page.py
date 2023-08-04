from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CatalogPage(BasePage):
    URL = "https://petstore.octoperf.com/actions/Catalog.action"
    EXPECTED_CATEGORIES = ["FISH", "DOGS", "CATS", "REPTILES", "BIRDS"]

    SIDEBAR_CATEGORY_TEMPLATE = "//div[@id='Sidebar']//a[contains(@href, '{category}')]"
    QUICK_LINKS_CATEGORY_TEMPLATE = "//div[@id='QuickLinks']//a[contains(@href, '{category}')]"
    MAIN_IMAGE_CONTENT_CATEGORY_TEMPLATE = "//div[@id='MainImageContent']//area[contains(@href, '{category}')]"

    FISH_CATEGORY = (By.XPATH, "//div[@id='Sidebar']//a[contains(@href, 'FISH')]")

    def click_fish_category(self):
        self.find(self.FISH_CATEGORY).click()

    def is_url_matches(self):
        return self.driver.current_url == self.URL

    def verify_categories_in_sidebar_present(self):
        for expected_category in self.EXPECTED_CATEGORIES:
            locator = (By.XPATH, self.SIDEBAR_CATEGORY_TEMPLATE.format(category=expected_category))
            assert self.find(locator)

    def verify_categories_in_quick_links_present(self):
        for expected_category in self.EXPECTED_CATEGORIES:
            locator = (By.XPATH, self.QUICK_LINKS_CATEGORY_TEMPLATE.format(category=expected_category))
            assert self.find(locator)

    def verify_categories_in_main_image_content_present(self):
        for expected_category in self.EXPECTED_CATEGORIES:
            locator = (By.XPATH, self.MAIN_IMAGE_CONTENT_CATEGORY_TEMPLATE.format(category=expected_category))
            assert self.find(locator)