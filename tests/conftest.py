import pytest
from selenium.webdriver import Chrome

from pages.catalog_page import CatalogPage
from pages.sign_in_page import SignInPage
from utils.utils import get_rand_value, get_rand_num


@pytest.fixture
def driver():
    driver = Chrome()
    driver.get("https://petstore.octoperf.com/actions/Catalog.action")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def username():
    return "0f01c5c"


@pytest.fixture(scope="session")
def password():
    return "0f01c5c"


@pytest.fixture
def uniq_value():
    return get_rand_value()


@pytest.fixture
def uniq_num():
    return get_rand_num()


@pytest.fixture
def logged_in_catalog_page(driver, username, password):
    catalog_page = CatalogPage(driver)
    catalog_page.click_sign_in()

    sign_in_page = SignInPage(driver)
    sign_in_page.enter_username(username)
    sign_in_page.enter_password(password)
    sign_in_page.click_login()

    return catalog_page