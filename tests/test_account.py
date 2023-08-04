from pages.catalog_page import CatalogPage
from pages.new_account_page import NewAccountPage
from pages.sign_in_page import SignInPage


def test_sign_in(driver, username, password):
    catalog_page = CatalogPage(driver)
    catalog_page.click_sign_in()

    sign_in_page = SignInPage(driver)
    sign_in_page.enter_username(username)
    sign_in_page.enter_password(password)
    sign_in_page.click_login()

    assert catalog_page.is_my_account_visible(), "My account is not visible"


def test_register(driver, uniq_value, uniq_num):
    catalog_page = CatalogPage(driver)
    catalog_page.click_sign_in()

    sign_in_page = SignInPage(driver)
    sign_in_page.click_register_now()

    new_account_page = NewAccountPage(driver)
    new_account_page.enter_username(uniq_value)
    new_account_page.enter_password(uniq_value)
    new_account_page.enter_account_data(uniq_value, uniq_value, uniq_value + "@gmail.com", uniq_num)
    new_account_page.enter_address_data(uniq_value, uniq_value, uniq_value, uniq_value, uniq_num, uniq_value)

    new_account_page.click_register()

    assert catalog_page.is_url_matches(), "URL is not correct"


def test_sign_out(logged_in_catalog_page):
    logged_in_catalog_page.click_sign_out()

    assert logged_in_catalog_page.is_sign_in_visible(), "Sign in is not visible"