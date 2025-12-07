from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalculatorPage:
    """Класс для работы с калькулятором, который включает в себя
    запуск драйвера, открытие браузера, установку таймера ожидания,
    функцию клика по кнопке, содержащей определённый текст. 
    А также последовательное нажатие по кнопкам калькулятора,
    получение результата и его ожидание по истечении таймера."""

    """Переменные с локаторами окна таймера и окошка с выводом результата"""
    delay_input = (By.CSS_SELECTOR, "#delay")
    result_screen = (By.CSS_SELECTOR, ".screen")

    @allure.step("Запуск драйвера, установка ожидания")
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    @allure.step("Установка таймера")
    def set_delay(self, delay_seconds: str):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.click()
        delay_element.clear()
        delay_element.send_keys(delay_seconds)

    @allure.step("Клик по нужной кнопке")
    def click_button(self, text: str):
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_locator).click()

    @allure.step("Клик по операторам")
    def calculation(self, num1: str, operator: str, num2: str):
        self.click_button(num1)
        self.click_button(operator)
        self.click_button(num2)
        self.click_button("=")

    @allure.step("Получение результата в кач-ве элемента страницы (для дальнейшей проверки)")
    def get_result(self):
        return self.driver.find_element(*self.result_screen).text

    @allure.step("Ожидание результата, пока ожидаемое значение не появится на экране")
    def wait_for_result(self, expected_result: str):
        self.wait.until(EC.text_to_be_present_in_element(self.result_screen,
                                                         expected_result))
