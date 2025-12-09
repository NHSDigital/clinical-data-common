"""Greeting module for clinical-data-common.

This module provides a simple greeting function that can be used across
clinical data API products.
"""


def get_hello() -> str:
    """Return a greeting string.

    Returns:
        str: The string 'Hello, '

    Example:
        >>> from clinical_data_common import get_hello
        >>> message = get_hello()
        >>> print(f"{message}World")
        Hello, World
    """
    return "Hello, "
