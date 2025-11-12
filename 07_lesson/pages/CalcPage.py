from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    # Переменные поля с таймером и с окном результата
    delay_input = (By.CSS_SELECTOR, "#delay")
    result_screen = (By.CSS_SELECTOR, ".screen")

    # Запуск драйвера
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    # Обозначение таймера
    def set_delay(self, delay_seconds: str):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.click()
        delay_element.clear()
        delay_element.send_keys(delay_seconds)

    # Клик по кнопкам калькулятора по их видимому тексту
    def click_button(self, text: str):
        button_locator = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button_locator).click()

    # Последовательное нажатие для вычисления суммы
    def calculator_sum(self, num1: str, operator: str, num2: str):
        self.click_button(num1)
        self.click_button(operator)
        self.click_button(num2)
        self.click_button("=")

    def get_result(self):
        return self.driver.find_element(*self.result_screen).text

    # Ожидание результата
    def wait_for_result(self, expected_result: str):
        self.wait.until(EC.text_to_be_present_in_element(self.result_screen,
                                                         expected_result))
