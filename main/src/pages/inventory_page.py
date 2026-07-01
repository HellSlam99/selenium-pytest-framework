from selenium.webdriver.common.by import By

from main.src.pages.base_page import BasePage


class InventoryPage(BasePage):

    CART = (By.CLASS_NAME, "shopping_cart_link")

    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):

        super().__init__(driver)

    def add_item(self, item_name):

        locator = (
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        )

        self.click(locator)

    def remove_item(self, item_name):

        locator = (
            By.XPATH,
            f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        )

        self.click(locator)

    def open_cart(self):

        self.click(self.CART)

    def get_cart_count(self):

        if self.is_visible(self.CART_BADGE):

            return int(self.get_text(self.CART_BADGE))

        return 0

    def get_page_title(self):

        return self.get_text(self.TITLE)