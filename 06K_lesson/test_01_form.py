import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService


def test_fields():
    edge_driver_path = r"C:\Users\Екатерина\Desktop\Marshstash\УЧЁБА\GitHub\repo_1\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))

    driver.get("https://www.google.com/")

    driver.maximize_window()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.implicitly_wait(20)

    first_name = driver.find_element(By.CSS_SELECTOR, '[name="first-name"]')
    first_name.click()
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, '[name="last-name"]')
    last_name.click()
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, '[name="address"]')
    address.click()
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]')
    email.click()
    email.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.CSS_SELECTOR, '[name="phone"]')
    phone_number.click()
    phone_number.send_keys("+7985899998787")

    city = driver.find_element(By.CSS_SELECTOR, '[name="city"]')
    city.click()
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, '[name="country"]')
    country.click()
    country.send_keys("Россия")

    job_position = driver.find_element(By.CSS_SELECTOR, '[name="job-position"]')
    job_position.click()
    job_position.send_keys("QA")

    company_name = driver.find_element(By.CSS_SELECTOR, '[name="company"]')
    company_name.click()
    company_name.send_keys("SkyPro")

    driver.implicitly_wait(10)
    submit_btn = driver.find_element(By.CSS_SELECTOR, '[type="submit"]')
    submit_btn.click()

    zip_selector = "#zip-code"
    zip_code_element = driver.find_element(By.CSS_SELECTOR, zip_selector)
    zip_code_color = zip_code_element.value_of_css_property("background-color")

    expected_red = "rgba(248, 215, 218, 1)"
    expected_green = "rgba(209, 231, 221, 1)"

    assert zip_code_color == expected_red

    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city",
              "country", "job-position", "company"]

    for field_name in fields:
        field_selector = f'[id="{field_name}"]'

        field_element = driver.find_element(By.CSS_SELECTOR, field_selector)
        field_color = field_element.value_of_css_property("background-color")

        assert field_color == expected_green

    driver.quit()
