from types import ModuleType
import os
from typing import Any


def error_message_details(error: Any, error_detail: ModuleType) -> str:
    """
    Extracts detailed error information, including the filename and line number.

    Args:
        error (Any): The exception object or error message that was raised.
        error_detail (ModuleType): The `sys` module, which is used to extract
            the traceback information via `sys.exc_info()`.

    Returns:
        str: A formatted error message detailing the script name, line number,
            and the original error.
    """
    exc_type, exc_value, exc_tb = error_detail.exc_info()

    if exc_tb is None:
        return f"[unknown:0] - {str(error)}"

    # Get the full path
    full_path: str = os.path.abspath(exc_tb.tb_frame.f_code.co_filename)

    line_number: int = exc_tb.tb_lineno

    # I removed the brackets here so it looks cleaner next to the logger's brackets
    error_message = f"Error in {full_path} at line {line_number}: {str(error)}"

    return error_message


class CustomException(Exception):
    """
    A custom exception class designed to capture and format detailed traceback
    information for easier debugging and logging.
    """

    def __init__(self, error: Any, error_detail: ModuleType) -> None:
        """
        Initializes the CustomException and generates the detailed error message.

        Args:
            error (Any): The exception object or error message that was raised.
            error_detail (ModuleType): The `sys` module, used to extract the
                traceback details.
        """
        super().__init__(str(error))
        self.error_message: str = error_message_details(error, error_detail)
        self.error_detail: ModuleType = error_detail

    def __str__(self) -> str:
        """
        Returns the formatted error message when the exception is printed or
        converted to a string.

        Returns:
            str: The detailed error message containing the filename, line number,
                and original error.
        """
        return self.error_message