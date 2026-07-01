import pytest

from main.src.utils.driver_factory import DriverFactory

from main.src.pages.login_page import LoginPage
from main.src.pages.inventory_page import InventoryPage
from main.src.pages.cart_page import CartPage
from main.src.pages.checkout_page import CheckoutPage
from main.src.pages.success_page import SuccessPage
from main.src.utils.screenshot import Screenshot
from main.src.utils.logger import Logger

logger = Logger.get_logger()

def pytest_addoption(parser):

    parser.addoption(

        "--browser",

        action="store",

        default="chrome",

        help="Browser Name"

    )

@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["app"]["driver"]

        Screenshot.capture(

            driver,

            report.nodeid.replace("::","_")

        )

@pytest.fixture()

def app(request):

    browser = request.config.getoption("--browser")

    driver = DriverFactory.get_driver(browser)

    login = LoginPage(driver)

    login.open_login_page()

    pages = {

        "driver": driver,

        "login": login,

        "inventory": InventoryPage(driver),

        "cart": CartPage(driver),

        "checkout": CheckoutPage(driver),

        "success": SuccessPage(driver)

    }
    logger.info(f"START : {request.node.name}")
    yield pages
    logger.info(f"END : {request.node.name}")
    driver.quit()
