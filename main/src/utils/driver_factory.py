from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from main.src.utils.config_reader import ConfigReader
from main.src.utils.logger import Logger


class DriverFactory:
    logger = Logger.get_logger()
    @staticmethod
    def get_driver(browser=None):

        config = ConfigReader()

        browser = browser or config.get_browser()

        browser = browser.lower()

        headless = config.is_headless()

        DriverFactory.logger.info(f"Launching Browser : {browser}")

        if browser == "chrome":

            options = ChromeOptions()

            if headless:
                options.add_argument("--headless=new")

            options = ChromeOptions()

            options.add_argument("--start-maximized")

            options.add_argument("--disable-notifications")

            options.add_argument("--disable-save-password-bubble")

            options.add_argument("--disable-popup-blocking")

            options.add_experimental_option(
                "excludeSwitches",
                ["enable-automation"]
            )

            options.add_experimental_option(
                "useAutomationExtension",
                False
            )

            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }

            options.add_experimental_option(
                "prefs",
                prefs
            )

            driver = webdriver.Chrome(
                service=ChromeService(
                    ChromeDriverManager().install()
                ),
                options=options
            )

        elif browser == "firefox":

            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            driver = webdriver.Firefox(
                service=FirefoxService(
                    GeckoDriverManager().install()
                ),
                options=options
            )

            driver.maximize_window()

        elif browser == "edge":

            options = EdgeOptions()

            if headless:
                options.add_argument("--headless=new")

            driver = webdriver.Edge(
                service=EdgeService(
                    EdgeChromiumDriverManager().install()
                ),
                options=options
            )

            driver.maximize_window()

        else:
            raise Exception(f"Unsupported Browser : {browser}")

        driver.implicitly_wait(0)

        return driver