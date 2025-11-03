from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://www.google.com/")

driver.maximize_window()

driver.get("http://uitestingplayground.com/textinput")

btn_input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
btn_input.send_keys("SkyPro")

blue_btn = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
blue_btn.click()

txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text

print(txt)

driver.quit()
