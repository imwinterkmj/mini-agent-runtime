"""Logging configuration for the runtime.

Phase 0 exercise: expose a small function that configures the standard-library
logger. Keep configuration here so later runtime modules do not each configure
their own handlers.
"""

import logging


def configure_logging(level: int = logging.INFO) -> None:
    """Configure application logging with a readable console format."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
