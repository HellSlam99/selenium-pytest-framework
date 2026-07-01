from selenium.webdriver.common.by import By

from main.src.pages.base_page import BasePage


class CartPage(BasePage):

    CHECKOUT = (By.ID, "checkout")

    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):

        super().__init__(driver)

    def remove_item(self, item_name):

        locator = (

            By.XPATH,

            f"//div[text()='{item_name}']/ancestor::div[@class='cart_item']//button"

        )

        self.click(locator)

    def get_cart_items(self):

        return self.get_elements(self.CART_ITEMS)

    def get_cart_count(self):

        return len(self.get_cart_items())

    def checkout(self):

        self.click(self.CHECKOUT)