import logging
import os
from datetime import datetime


class LogGen:

    @staticmethod
    def loggen():

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        log_file = os.path.join(
            log_dir,
            f"automation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )

        logger = logging.getLogger("AutomationLogger")
        logger.setLevel(logging.INFO)

        # Prevent duplicate handlers
        if not logger.handlers:

            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )
            file_handler.setFormatter(formatter)

            logger.addHandler(file_handler)

        return logger

