"""Minimal test proving that the src-layout package is importable."""

import mini_agent


def test_package_version() -> None:
    assert mini_agent.__version__ == "0.1.0"

