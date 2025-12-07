import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.LoginPage import LoginPage
from pages.ShopPage import ShopPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
import allure


@pytest.fixture(scope="function")
def driver_setup():
    
     manager = GeckoDriverManager()
     service = FirefoxService(manager.install())
     driver = webdriver.Firefox(service=service)
   
     driver.maximize_window()
    
     driver.get("https://www.saucedemo.com")
     driver.implicitly_wait(10)
    
     yield driver
     driver.quit()


@allure.id("SHOP-1")
@allure.severity("P2")
@allure.epic("Интернет магазин")
@allure.feature("Оформление заказа")
@allure.title("Тест успешного заказа в Интернет-магазине")
@allure.description("Тест включает в себя авторизацию, добавление товаров в корзину," \
"переход на страницу Корзины, оформление заказа и проверка итоговой цены")
def test_successful_order(driver_setup):
    driver = driver_setup

    with allure.step("Инициализация страниц"):
        login_page = LoginPage(driver)
        shop_page = ShopPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

    with allure.step("Открытие страницы авторизации, заполнение полей логина и пароля"):
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        shop_page.add_item_to_cart(ShopPage.backpack)
        shop_page.add_item_to_cart(ShopPage.tshirt)
        shop_page.add_item_to_cart(ShopPage.onesie)

    with allure.step("Переход на страницу Корзины"):
        shop_page.go_to_cart()

    with allure.step("Открытие страницы для оформления заказа"):
        cart_page.proceed_to_checkout()

    with allure.step("Заполнение полей для оформления заказа"):
        first_name = "Anna"
        last_name = "Spanacopita"
        zip_code = "605126"
        checkout_page.fill_info(first_name, last_name, zip_code)
    with allure.step("Клик по кнопке Continue"):
        checkout_page.click_continue()

    """Получение фактических данных итоговой суммы для сравнения с ожидаемыми"""
    expected_total_text = "Total: $58.29"
    actual_total_text = checkout_page.get_total()

    with allure.step("Проверка фактической итоговой суммы с ожидаемой и вывод данных в консоль после тест-рана"):
        print(f"{actual_total_text}")
        assert actual_total_text == expected_total_text
