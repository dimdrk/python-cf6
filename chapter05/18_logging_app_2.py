import logging
from typing import List, Any

def configure_logger(log_file: str, logger_name: str) -> logging.Logger:
    """
    Configure and return a logger with both file and console handlers.

    Args:
        log_file (str): The name of the log file.
        logger_name (str): The name of the logger.

    Returns:
        logging.Logger: Configures logger instance.
    """
    # Create the logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)   # Set the logging level

    # # Level # | # Sensitivity #
    # DEBUG     | Lowest
    # INFO      | Low
    # WARNING   | Medium
    # ERROR     | High
    # CRITICAL  | Highest

    # File handler (for logging to a file)
    file_handler = logging.FileHandler(log_file, mode='a')
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s%(levelname)s%(name)s%(message)s")
    )
    # # Mode #  | # Purpose #
    #   'a'     | Append
    #   'w'     | Write
    #   'r'     | Read
    #   'b'     | Binary
    #   'r+'    | Read + Write
    #   'w+'    | Write + Read

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter("%(asctime)s%(levelname)s%(name)s%(message)s")
    )

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def search_item(items: List[Any], item_to_find: Any, logger: logging.Logger) -> int:
    """
    Search for an item in a list and return its index.

    Args:
        items (List[Any]): List of items to search within.
        item_to_find (Any): The item to find.
        logger (logging.Logger): Logger instance for logging messages.

    Returns:
        int: The index of the item in the list.

    Raises:
        ValueError: If the item is not found.
    """
    if not items:
        logging.warning("The list is empty.")
        raise ValueError("Cannot search in an empty list.")
    
    try:
        index = items.index(item_to_find)
        logger.info(f"Item {item_to_find} found at index: {index}.")
        return index
    except ValueError as e:
        logger.error(f"Item {item_to_find} not found in the list. Error: {e}.", exc_info=True)
        raise   # Re-raise the same ValueError

def main():
    # Log file name
    log_file = 'search_cf6.log'

    # Create a logger
    logger = configure_logger(log_file, 'search-app')

    # List of employee names
    employee_names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    employee_to_find = "Alice"

    try:
        index = search_item(employee_names, employee_to_find, logger)
        print(f"Employee '{employee_to_find}' found at index: {index}.")
    except ValueError:
        print(f"Employee '{employee_to_find}' was not found in the list.")



if __name__ == '__main__':
    main()