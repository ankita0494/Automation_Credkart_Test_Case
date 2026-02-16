import logging
import os

class log_generator_class:
    @staticmethod# without crating class object
    def log_gen_method():#method
        log_dir = ".\\Logs"
        os.makedirs(log_dir, exist_ok=True)

        logger = logging.getLogger("CredkartLogger")
        logger.setLevel(logging.INFO)

        if not logger.handlers:  # ⭐ THIS IS VERY IMPORTANT
            log_file = logging.FileHandler(f"{log_dir}\\Credkart_Test_Automation.log")
            log_format = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s-%(lineno)d - %(message)s"
            )
            log_file.setFormatter(log_format)
            logger.addHandler(log_file)

        return logger

#type of log levels
#debug
#info
#warning
#error
#critical
