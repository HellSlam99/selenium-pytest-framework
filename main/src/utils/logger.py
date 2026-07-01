import logging

import os

from datetime import datetime

from main.src.utils.constants import REPORT_FOLDER


class Logger:

    @staticmethod
    def get_logger():

        logger = logging.getLogger("SauceDemo")

        if logger.hasHandlers():
            return logger

        logger.setLevel(logging.INFO)

        os.makedirs(REPORT_FOLDER, exist_ok=True)

        logfile = os.path.join(
            REPORT_FOLDER,
            f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )

        file_handler = logging.FileHandler(logfile)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger