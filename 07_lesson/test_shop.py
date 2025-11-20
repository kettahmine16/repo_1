import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.LoginPage import LoginPage
from pages.ShopPage import ShopPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage


@pytest.fixture
# Открытие браузера и страницы Магазина
def driver_setup():
    manager = GeckoDriverManager()
    service = FirefoxService(manager.install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_successful_order(driver_setup):
    driver = driver_setup

    login_page = LoginPage(driver)
    shop_page = ShopPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    shop_page.add_item_to_cart(ShopPage.backpack)
    shop_page.add_item_to_cart(ShopPage.tshirt)
    shop_page.add_item_to_cart(ShopPage.onesie)

    shop_page.go_to_cart()

    cart_page.proceed_to_checkout()

    first_name = "Anna"
    last_name = "Spanacopita"
    zip_code = "605126"
    checkout_page.fill_info(first_name, last_name, zip_code)
    checkout_page.click_continue()

    expected_total_text = "Total: $58.29"
    actual_total_text = checkout_page.get_total()

    print(f"{actual_total_text}")
    assert actual_total_text == expected_total_text
