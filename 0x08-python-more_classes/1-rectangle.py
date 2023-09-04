#!/usr/bin/python3
"""Defines a Rectangle class.

Private instance attributes:
    - __width: Width of the rectangle.
    - __height: Height of the rectangle.

Public methods:
    - __init__(self, width=0, height=0): Initializes a rectangle with optional width and height.

Properties:
    - width: Gets or sets the width of the rectangle.
    - height: Gets or sets the height of the rectangle.
"""

class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = 0  # Initialize width with 0
        self.__height = 0  # Initialize height with 0
        self.width = width  # Call the width setter to set the width
        self.height = height  # Call the height setter to set the height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

