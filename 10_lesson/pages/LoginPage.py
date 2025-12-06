from selenium.webdriver.common.by import By
import allure


class LoginPage:
    """Класс содержит в себе инициализацию драйвера и функции для работы с полями на странице авторизации,
    а также список необходимых переменных.
    Переменные: URL, локатор поля User Name, Password и кнопки Login"""

    url = "https://www.saucedemo.com"
    user_name_field = (By.CSS_SELECTOR, "#user-name")
    password_field = (By.CSS_SELECTOR, "#password")
    login_button = (By.CSS_SELECTOR, "#login-button")

    @allure.step("Запуск драйвера")
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открытие нужного URL")
    def open(self):
        self.driver.get(self.url)

    @allure.step("Поиск элемента по локатору и последующий ввод данных в поля. Клик по кнопке авторизации.")
    def login(self, username, password):
        self.driver.find_element(*self.user_name_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
