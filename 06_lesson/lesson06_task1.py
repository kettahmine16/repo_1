from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://www.google.com/")

driver.maximize_window()

driver.get("http://uitestingplayground.com/ajax")
wait = WebDriverWait(driver, 20)

press_btn = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "#ajaxButton")))
press_btn.click()

expected_text = "Data loaded with AJAX get request."
wait.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "p.bg-success"),
        expected_text
    )
)

flash_success_element = driver.find_element(By.CSS_SELECTOR, "p.bg-success")
txt = flash_success_element.text

print(txt)

driver.quit()
