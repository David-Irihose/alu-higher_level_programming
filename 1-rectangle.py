#!/usr/bin/python3
"""
Module: 1-rectangle
Defines a Rectangle class with private width and height,
including getters and setters with validation.
"""


class Rectangle:
    """
    A class that defines a rectangle by its width and height.

    Private Attributes:
        __width (int): width of the rectangle
        __height (int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance with optional width and height.

        Args:
            width (int): width of the rectangle (default 0)
            height (int): height of the rectangle (default 0)

        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle with validation.

        Args:
            value (int): width value to set

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle with validation.

        Args:
            value (int): height value to set

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
