"""Tests for smart-manifest-gen."""

import pytest
from smart_manifest_gen import gen


class TestGen:
    """Test suite for gen."""

    def test_basic(self):
        """Test basic usage."""
        result = gen("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            gen("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = gen(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
