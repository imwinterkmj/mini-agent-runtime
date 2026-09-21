"""Command-line entry point for mini-agent-runtime."""

import logging

from mini_agent.logging_config import configure_logging

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the current learning-stage demo."""
    configure_logging()
    logger.info("mini-agent-runtime started")


if __name__ == "__main__":
    main()
