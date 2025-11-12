from selenium.webdriver.common.by import By


class CheckoutPage:
    first_name_field = (By.CSS_SELECTOR, "#first-name")
    last_name_field = (By.CSS_SELECTOR, "#last-name")
    zip_code_field = (By.CSS_SELECTOR, "#postal-code")
    continue_button = (By.CSS_SELECTOR, "#continue")
    total_label = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def fill_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(*self.zip_code_field).send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        return self.driver.find_element(*self.total_label).text
