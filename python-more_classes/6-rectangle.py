#!/usr/bin/python3
"""class module"""


class Rectangle:
    """Class Rectangle public class atribute number_of_instances"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Initialization method"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    
    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """String representation"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = ""
        for i in range(self.__height):
            rect += "#" * self.__width + "\n"
        return rect[:-1]

    def __repr__(self):
        """Representation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
