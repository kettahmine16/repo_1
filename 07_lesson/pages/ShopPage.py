from selenium.webdriver.common.by import By


class ShopPage:
    backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    tshirt = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
    cart_icon = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_locator):
        self.driver.find_element(*item_locator).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
