import logging
import coloredlogs

def setup_logging():
    """Configure root logger to DEBUG level with colored logs and a simple format."""
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    # Set up base logging config
    logging.basicConfig(level=logging.INFO, format=log_format)

    # Add colored logs to the root logger
    coloredlogs.install(level='INFO', fmt=log_format)

    return logging