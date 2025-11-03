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

driver.implicitly_wait(40)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

images = WebDriverWait(driver, 40).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container"))
)

find_src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

print(find_src)

driver.quit()
