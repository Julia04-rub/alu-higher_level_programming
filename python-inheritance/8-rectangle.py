#!/usr/bin/python3
"""Class Rectanglr inheritd from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """define rectangle"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
