from selenium.webdriver.common.by import By

from main.src.pages.base_page import BasePage
from main.src.utils.config_reader import ConfigReader


class LoginPage(BasePage):

    USERNAME = (By.ID, "user-name")

    PASSWORD = (By.ID, "password")

    LOGIN = (By.ID, "login-button")

    ERROR = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):

        super().__init__(driver)

        self.config = ConfigReader()

    def open_login_page(self):

        self.open(self.config.get_base_url())

    def enter_username(self, username):

        self.type(self.USERNAME, username)

    def enter_password(self, password):

        self.type(self.PASSWORD, password)

    def click_login(self):

        self.click(self.LOGIN)

    def login(self, username, password):

        self.enter_username(username)

        self.enter_password(password)

        self.click_login()

    def get_error_message(self):

        return self.get_text(self.ERROR)

    def is_login_successful(self):

        return "inventory.html" in self.get_url()