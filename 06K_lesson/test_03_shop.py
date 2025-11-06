from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_shop():
    driver = webdriver.Firefox(service=FirefoxService
                               (GeckoDriverManager().install()))

    driver.get("https://www.saucedemo.com")
    driver.implicitly_wait(5)

    user_name = driver.find_element(By.CSS_SELECTOR, "#user-name")
    user_name.click()
    user_name.send_keys("standard_user")

    password = driver.find_element(By.CSS_SELECTOR, "#password")
    password.click()
    password.send_keys("secret_sauce")

    login_btn = driver.find_element(By.CSS_SELECTOR, "#login-button")
    login_btn.click()
    driver.implicitly_wait(10)

    add_button_backpack = "#add-to-cart-sauce-labs-backpack"
    add_to_cart = driver.find_element(By.CSS_SELECTOR, add_button_backpack)
    add_to_cart.click()

    add_button_tshirt = "#add-to-cart-sauce-labs-bolt-t-shirt"
    add_to_cart_2 = driver.find_element(By.CSS_SELECTOR, add_button_tshirt)
    add_to_cart_2.click()

    add_button_onesie = "#add-to-cart-sauce-labs-onesie"
    add_to_cart_3 = driver.find_element(By.CSS_SELECTOR, add_button_onesie)
    add_to_cart_3.click()

    cart_locator = ".shopping_cart_link"
    cart = driver.find_element(By.CSS_SELECTOR, cart_locator)
    cart.click()
    driver.implicitly_wait(5)

    checkout_btn = driver.find_element(By.CSS_SELECTOR, "#checkout")
    checkout_btn.click()

    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.click()
    first_name.send_keys("Anna")

    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.click()
    last_name.send_keys("Spanacopita")

    zip_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    zip_code.click()
    zip_code.send_keys("605126")

    continue_btn = driver.find_element(By.CSS_SELECTOR, "#continue")
    continue_btn.click()
    driver.implicitly_wait(10)

    total_css_selector = ".summary_total_label"
    expected_total_text = "Total: $58.29"

    actual_total_text = driver.find_element(By.CSS_SELECTOR,
                                            total_css_selector).text

    print(actual_total_text)
    assert actual_total_text == expected_total_text

    driver.quit()
