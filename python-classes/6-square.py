#!/usr/bin/python3
"""
This module defines a Square class with private size and position attributes,
getter and setter for both, area computation, and printing the square
taking the position into account.
"""


class Square:
    """Represent a square with size, position, area method, and printing."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with optional size and position.

        Args:
            size (int): Size of the square (default 0).
            position (tuple): Coordinates for printing the square (default (0, 0)).

        Raises:
            TypeError: If size is not an integer or position is not a tuple
                       of 2 positive integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(n, int) for n in value)
            or not all(n >= 0 for n in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute and return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the character '#' taking position into account."""
        if self.__size == 0:
            print()
            return

        # Print vertical offset
        for _ in range(self.__position[1]):
            print()

        # Print each row of the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
