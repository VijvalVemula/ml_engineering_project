import sys
import logging
import logger
from exception import CustomException


def trigger_intentional_error():
    """A dummy function designed to fail so we can test our pipeline."""
    try:
        # This will cause a ZeroDivisionError
        result = 10 / 0
    except Exception as e:
        # We catch the standard error and wrap it in our CustomException
        raise CustomException(e, sys)


if __name__ == "__main__":
    # Log a standard info message to prove the logger is working
    logging.info("Starting the test script...")

    try:
        trigger_intentional_error()
    except CustomException as ce:
        # Catch our custom exception and log the formatted string as an ERROR
        logging.error(ce)

    logging.info("Test script finished executing.")