import pytest
from pages.CalcPage import CalculatorPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
# Открытие браузера и страницы Калькулятора
def driver_setup():
    manager = ChromeDriverManager()
    service = ChromeService(manager.install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_calculation(driver_setup):
    driver = driver_setup
    CalcPage = CalculatorPage(driver)

    # Установка таймера
    delay_value = "45"
    CalcPage.set_delay(delay_value)

    # Выполнение вычисления
    CalcPage.calculator_sum(
        num1="7",
        operator="+",
        num2="8",
    )

    # Ожидание результата
    expected_result = "15"
    CalcPage.wait_for_result(expected_result)
    actual_result = CalcPage.get_result()
    assert actual_result == expected_result
