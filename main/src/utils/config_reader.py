from configparser import ConfigParser

from main.src.utils.constants import CONFIG_FILE


class ConfigReader:

    def __init__(self):
        self.parser = ConfigParser()
        self.parser.read(CONFIG_FILE)

    def get_base_url(self):
        return self.parser.get("DEFAULT", "BASE_URL")

    def get_browser(self):
        return self.parser.get("DEFAULT", "BROWSER")

    def get_timeout(self):
        return self.parser.getint("DEFAULT", "TIMEOUT")

    def is_headless(self):
        return self.parser.getboolean("DEFAULT", "HEADLESS")

    def get_log_path(self):
        return self.parser.get("DEFAULT", "LOG_PATH")

    def get_screenshot_path(self):
        return self.parser.get("DEFAULT", "SCREENSHOT_PATH")