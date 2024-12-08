import logging

def main():
    log_file = 'cf6.log'

    # Create a file handler for logging to a file
    file_handler = logging.FileHandler(log_file, mode='a')

    # Create a list of handlers
    handlers = [file_handler]

    # Create a logger
    logger = logging.getLogger('search-app')

    # Configuration
    logging.basicConfig(
        handlers=handlers,
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s%(name)s%(message)s"
    )

    nums = [10, 20, 30, 40, 50]

    try:
        index = nums.index(330)
        print("Found!")
        print(index)
    except ValueError as e:
        # Log an error
        logger.error(f"Error occured: {e}", exc_info=True)

if __name__ == '__main__':
    main()