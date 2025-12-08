"""Unit tests for the greeting module."""

import pytest
from clinical_data_common.greeting import get_hello


class TestGetHello:
    """Test suite for the get_hello function."""

    def test_get_hello_returns_correct_string(self):
        """Test that get_hello returns 'Hello, ' exactly."""
        result = get_hello()
        assert result == "Hello, "

    def test_get_hello_returns_string_type(self):
        """Test that get_hello returns a string type."""
        result = get_hello()
        assert isinstance(result, str)

    def test_get_hello_has_trailing_space(self):
        """Test that get_hello has a trailing space for concatenation."""
        result = get_hello()
        assert result.endswith(" ")

    def test_get_hello_can_be_concatenated(self):
        """Test that get_hello can be concatenated with other strings."""
        result = get_hello()
        full_message = f"{result}World"
        assert full_message == "Hello, World"
