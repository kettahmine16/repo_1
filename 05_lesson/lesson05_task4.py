from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService
                           (GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")

username_locator = "#username"
username_input = driver.find_element(By.CSS_SELECTOR, username_locator)

username_input.send_keys("tomsmith")

password_locator = "#password"
password_input = driver.find_element(By.CSS_SELECTOR, password_locator)

password_input.send_keys("SuperSecretPassword!")

sleep(3)

login_btn = "i"
press_login_btn = driver.find_element(By.CSS_SELECTOR, login_btn)

press_login_btn.click()


flash_success = "div#flash.flash.success"
flash_success_locator = driver.find_element(By.CSS_SELECTOR, flash_success)

print(flash_success_locator.text)

driver.quit()
