import logging
import os
import sys
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)
LOG_FILE_PATH = os.path.join(LOGS_DIR, LOG_FILE)

logging.basicConfig(
    format="[%(asctime)s:%(filename)s:%(lineno)d] - %(levelname)s \t - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

if __name__ == "__main__":
    logging.info("Logging configuration setup complete.")