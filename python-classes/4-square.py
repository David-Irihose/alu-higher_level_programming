#!/usr/bin/python3
"""
This module defines a Square class with private size attribute,
getter and setter for size, and a method to compute the square area.
"""


class Square:
    """Represent a square with a private size, getter/setter, and area method."""

    def __init__(self, size=0):
        """
        Initialize the square with optional size.

        Args:
            size (int): Size of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Will use the setter for validation

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): New size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Compute and return the area of the square.

        Returns:
            int: The current square area.
        """
        return self.__size ** 2
