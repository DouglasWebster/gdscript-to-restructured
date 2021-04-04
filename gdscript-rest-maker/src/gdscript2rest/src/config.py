import logging

LOGGER = logging.getLogger("GDScript rest maker")
LOG_LEVELS = [logging.INFO, logging.DEBUG]
LOG_LEVELS = [None] + sorted(LOG_LEVELS, reverse=True)
