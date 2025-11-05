#!/usr/bin/python3
"""
This module defines a Square class with size validation.
The size attribute is private and must be an integer >= 0.
"""


class Square:
    """Represent a square with a validated private size attribute."""

    def __init__(self, size=0):
        """
        Initialize the square with optional size.

        Args:
            size (int): Size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
