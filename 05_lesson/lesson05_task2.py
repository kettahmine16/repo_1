from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# Открыть браузер Google Chrome
driver.get("https://www.google.com/")

driver.maximize_window()

# Перейти на страницу: http://uitestingplayground.com/dynamicid
driver.get("http://uitestingplayground.com/dynamicid")
sleep(3)

# Нажать на синюю кнопку
blue_button = ".btn.btn-primary"
push_button = driver.find_element(By.CSS_SELECTOR, blue_button)

push_button.click()

sleep(5)

driver.quit()
