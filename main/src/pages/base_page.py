from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException

from main.src.utils.logger import Logger

from main.src.utils.screenshot import Screenshot

from main.src.utils.config_reader import ConfigReader


class BasePage:

    def __init__(self, driver):

        self.driver = driver

        self.logger = Logger.get_logger()

        self.timeout = ConfigReader().get_timeout()

        self.wait = WebDriverWait(
            driver,
            self.timeout
        )

    ########################################################

    def open(self, url):

        self.logger.info(f"Opening URL : {url}")

        self.driver.get(url)

        Screenshot.capture(
            self.driver,
            "Open_URL"
        )

    ########################################################

    def find(self, locator):

        return self.wait.until(

            EC.visibility_of_element_located(locator)

        )

    ########################################################

    def click(self, locator):

        element = self.find(locator)

        element.click()

        self.logger.info(f"Clicked : {locator}")

        Screenshot.capture(
            self.driver,
            "Click"
        )

    ########################################################

    def type(self, locator, text):

        element = self.find(locator)

        element.clear()

        element.send_keys(text)

        self.logger.info(
            f"Entered Text : {text}"
        )

        Screenshot.capture(
            self.driver,
            "Type"
        )

    ########################################################

    def get_text(self, locator):

        element = self.find(locator)

        value = element.text

        self.logger.info(
            f"Captured Text : {value}"
        )

        return value

    ########################################################

    def is_visible(self, locator):

        try:

            self.find(locator)

            return True

        except TimeoutException:

            return False

    ########################################################

    def get_title(self):

        return self.driver.title

    ########################################################

    def get_url(self):

        return self.driver.current_url

    ########################################################

    def wait_until_clickable(self, locator):

        return self.wait.until(

            EC.element_to_be_clickable(locator)

        )

    ########################################################

    def wait_until_invisible(self, locator):

        return self.wait.until(

            EC.invisibility_of_element(locator)

        )

    ########################################################

    def scroll_into_view(self, locator):

        element = self.find(locator)

        self.driver.execute_script(

            "arguments[0].scrollIntoView();",

            element

        )

        Screenshot.capture(
            self.driver,
            "Scroll"
        )

    ########################################################

    def js_click(self, locator):

        element = self.find(locator)

        self.driver.execute_script(

            "arguments[0].click();",

            element

        )

        Screenshot.capture(
            self.driver,
            "JSClick"
        )

    ########################################################

    def get_elements(self, locator):

        return self.driver.find_elements(
            locator[0],
            locator[1]
        )

    ########################################################

    def quit(self):

        self.logger.info("Closing Browser")

        self.driver.quit()