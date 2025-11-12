from selenium.webdriver.common.by import By


class LoginPage:
    # Переменные
    url = "https://www.saucedemo.com"
    user_name_field = (By.CSS_SELECTOR, "#user-name")
    password_field = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.driver.find_element(*self.user_name_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
