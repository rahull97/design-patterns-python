# Liskov substitution principle states that the objects of a superclass should
# be replaceable with objects of its subclasses without breaking the
# application. The below example demonstrates the breaking of the above
# principle.


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"


def use_it(rc: Rectangle):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f"Expected an area of {expected}, got {rc.area}")


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


if __name__ == "__main__":
    rectangle = Rectangle(2, 3)
    use_it(rectangle)

    # use_it function gives incorrect result for subclass
    # thus breaking LSP.
    square = Square(5)
    use_it(square)
