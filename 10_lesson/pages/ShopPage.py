from selenium.webdriver.common.by import By
import allure


class ShopPage:
    """Класс содержит в себе переменные локаторов для обозначения кнопок, добавляющих нужные элементы в Корзину"""

    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
    cart_icon = (By.CSS_SELECTOR, ".shopping_cart_link")

    @allure.step("Запуск драйвера")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавление товара в Корзину методом клика на нужную кнопку")
    def add_item_to_cart(self, item_locator):
        self.driver.find_element(*item_locator).click()

    @allure.step("Переход на страницу Корзины")
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
