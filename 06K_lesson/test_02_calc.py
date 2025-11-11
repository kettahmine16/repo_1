from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

    driver.get("https://www.google.com/")

    driver.maximize_window()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.implicitly_wait(10)

    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.click()
    delay.clear()
    delay.send_keys("45")

    first_btn = driver.find_element(By.XPATH, "//span[text()='7']")
    first_btn.click()

    sum_btn = driver.find_element(By.XPATH, "//span[text()='+']")
    sum_btn.click()

    second_btn = driver.find_element(By.XPATH, "//span[text()='8']")
    second_btn.click()

    equal_btn = driver.find_element(By.XPATH, "//span[text()='=']")
    equal_btn.click()

    expected_result = "15"
    result_locator = (By.CSS_SELECTOR, ".screen")

    wait = WebDriverWait(driver, 50)

    wait.until(EC.text_to_be_present_in_element
               (result_locator, expected_result))
    result = driver.find_element(*result_locator)
    actual_result = result.text

    assert actual_result == expected_result

    driver.quit()
