from pages.cart_page import CartPage
from pages.category_page import CategoryPage
from pages.product_page import ProductPage


def test_buy_large_angelfish_from_product(driver, logged_in_catalog_page):
    logged_in_catalog_page.click_fish_category()

    category_page = CategoryPage(driver)
    category_page.click_angelfish()
    category_page.click_large_angelfish()

    product_page = ProductPage(driver)
    product_page.click_add_to_cart()

    cart_page = CartPage(driver)
    cart_page.verify_first_item_description_match("Large Angelfish")


def test_buy_large_angelfish_from_category(driver, logged_in_catalog_page):
    logged_in_catalog_page.click_fish_category()

    category_page = CategoryPage(driver)
    category_page.click_angelfish()
    category_page.click_large_angelfish_add_to_cart()

    cart_page = CartPage(driver)
    cart_page.verify_first_item_description_match("Large Angelfish")