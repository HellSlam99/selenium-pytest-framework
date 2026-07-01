import os

from datetime import datetime

from main.src.utils.constants import SCREENSHOT_FOLDER


class Screenshot:

    @staticmethod
    def capture(driver, name):

        os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

        filename = f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"

        path = os.path.join(
            SCREENSHOT_FOLDER,
            filename
        )

        driver.save_screenshot(path)

        return path