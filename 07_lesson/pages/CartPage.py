from selenium.webdriver.common.by import By


class CartPage:
    checkout_button = (By.CSS_SELECTOR, "#checkout")

    def __init__(self, driver):
        self.driver = driver

    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
