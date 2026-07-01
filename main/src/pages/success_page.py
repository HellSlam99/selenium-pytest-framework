from selenium.webdriver.common.by import By

from main.src.pages.base_page import BasePage


class SuccessPage(BasePage):

    MESSAGE = (By.CLASS_NAME, "complete-header")

    BACK_HOME = (By.ID, "back-to-products")

    def __init__(self, driver):

        super().__init__(driver)

    def get_success_message(self):

        return self.get_text(self.MESSAGE)

    def back_to_home(self):

        self.click(self.BACK_HOME)