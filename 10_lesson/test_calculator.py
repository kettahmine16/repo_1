import pytest
from pages.CalcPage import CalculatorPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import allure


@pytest.fixture
@allure.id("CALC-1")
@allure.severity("P1")
@allure.epic("Калькулятор")
@allure.feature("SETUP_DRIVER")
@allure.title("Запуск драйвера/браузера")
@allure.description("Запуск теста, открытие браузера и установка ожидания на время тест-рана")
def driver_setup():
    with allure.step("Инициализация браузера Chrome"):
        manager = ChromeDriverManager()
        service = ChromeService(manager.install())
        driver = webdriver.Chrome(service=service)
    with allure.step("Увеличить окно браузера"):
        driver.maximize_window()
    with allure.step("Открыть сайт с Калькулятором и ожидание на прогрузку страницы"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        driver.implicitly_wait(10)
    with allure.step("Ожидание браузера до окончания теста и выход из драйвера"):
        yield driver
        driver.quit()


@allure.id("CALC-2")
@allure.severity("P1")
@allure.epic("Калькулятор")
@allure.feature("TEST_CALCULATE")
@allure.title("Запуск калькулятора")
@allure.description("Тест функции калькулятора с установкой таймера, по истечении которого выводится ответ")
def test_calculation(driver_setup):
    with allure.step("Открытие браузера и сайта с Калькулятором"):
        driver = driver_setup
        CalcPage = CalculatorPage(driver)

    with allure.step("Установка таймера, по истечении которого калькулятор выдаст ответ"):
        delay_value = "45"
        CalcPage.set_delay(delay_value)

    with allure.step("Ввод в калькулятор данных, с которыми он будет проводить функцию"):
        CalcPage.calculation(
        num1="7",
        operator="+",
        num2="8",
    )

    with allure.step("Ожидание результата по истечении таймера и проверка вычисления"):
        expected_result = "15"
        CalcPage.wait_for_result(expected_result)
        with allure.step("Проверка ожидаемого результата с фактическим"):
            actual_result = CalcPage.get_result()
            assert actual_result == expected_result
