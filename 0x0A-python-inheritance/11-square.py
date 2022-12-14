#!/usr/bin/python3
"""
This is module 11-square
This module contains one function
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    inherits class from Rectangle (9-rectangle.py)
    Instantiation with width and height:
    Instantiation with size: def __init__(self, size)::
    size must be private. No getter or setter
    size must be a positive integer, validated by integer_validator
    Args:
    size
    Returns:
    area of shape
    """

    def __init__(self, size):
        """
        public instantiation
        """
        self.__size = size
        self.__width = size
        self.__height = size
        super().__init__(size, size)

    def __str__(self):
        """
        instance method for string - print class name with
        following rectangle description: [Rectangle] <width>/<height>
        """
        return ("[{:s}] {:d}/{:d}".
                format(__class__.__name__,
                       self.__width,
                       self.__height))
