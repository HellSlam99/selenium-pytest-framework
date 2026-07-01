from selenium.webdriver.common.by import By

from main.src.pages.base_page import BasePage


class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")

    LAST_NAME = (By.ID, "last-name")

    ZIP = (By.ID, "postal-code")

    CONTINUE = (By.ID, "continue")

    FINISH = (By.ID, "finish")

    def __init__(self, driver):

        super().__init__(driver)

    def enter_first_name(self, value):

        self.type(self.FIRST_NAME, value)

    def enter_last_name(self, value):

        self.type(self.LAST_NAME, value)

    def enter_zip(self, value):

        self.type(self.ZIP, value)

    def continue_checkout(self):

        self.click(self.CONTINUE)

    def finish_checkout(self):

        self.click(self.FINISH)

    def checkout(self, first, last, zip_code):

        self.enter_first_name(first)

        self.enter_last_name(last)

        self.enter_zip(zip_code)

        self.continue_checkout()

        self.finish_checkout()