from selenium.webdriver.common.by import By
import allure


class CartPage:
    """Класс содержит в себе функции для работы со страницей Корзины и переход на страницу Оформления заказа.
    Переменные: локатор кнопки, отправляющей на страницу Оформления заказа"""
    checkout_button = (By.CSS_SELECTOR, "#checkout")

    @allure.step("Запуск драйвера")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Запуск драйвера")
    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
