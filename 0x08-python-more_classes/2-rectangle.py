#!/usr/bin/python3
"""Defines a Rectangle class.

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception with the message "width must be an integer"
if width is less than 0, raise a ValueError exception with the message "width must be >= 0"

Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception with the message "height must be an integer"
if height is less than 0, raise a ValueError exception with the message "height must be >= 0"

Instantiation with optional width and height: def __init__(self, width=0, height=0):

Public instance method: def area(self): that returns the rectangle area

Public instance method: def perimeter(self): that returns the rectangle perimeter:
if width or height is equal to 0, perimeter is equal to 0

Public instance method: def display(self): that prints the rectangle with `#` symbols.

Public instance method: def __str__(self): that returns a string representation of the rectangle.
"""

class Rectangle:
    """Defines a Rectangle class.

    Private instance attributes:
        - __width: Width of the rectangle.
        - __height: Height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initializes a rectangle with optional width and height."""
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)

    def display(self):
        """Prints the rectangle using '#' symbols."""
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """Returns a string representation of the rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

