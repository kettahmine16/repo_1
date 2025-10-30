from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://www.google.com/")

driver.maximize_window()

driver.implicitly_wait(20)
driver.get("http://uitestingplayground.com/ajax")

blue_btn = "#ajaxButton"
press_btn = driver.find_element(By.CSS_SELECTOR, blue_btn)
press_btn.click()

flash_success = driver.find_element(By.CSS_SELECTOR, "#content")
txt = flash_success.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

driver.quit()
