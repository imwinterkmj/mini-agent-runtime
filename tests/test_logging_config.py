"""Tests for the application logging configuration."""

import logging

import pytest

from mini_agent.logging_config import configure_logging


def test_configure_logging_uses_level_and_required_fields(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: dict[str, object] = {}

    def fake_basic_config(**kwargs: object) -> None:
        captured.update(kwargs)

    monkeypatch.setattr(logging, "basicConfig", fake_basic_config)

    configure_logging(logging.DEBUG)

    assert captured["level"] == logging.DEBUG

    log_format = captured["format"]
    assert isinstance(log_format, str)
    for field in ("%(asctime)s", "%(levelname)s", "%(name)s", "%(message)s"):
        assert field in log_format
