# open close principle states that the classes should
# be closed for modification but open for extension

from enum import Enum


class Color(Enum):
    """Enum class for Color"""
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    """Enum class for Size"""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    """This class constructs new product"""

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    """
    This class demonstrates violation of ocp,
    as every time new filter needs to be added,
    this class gets modified.
    """

    @staticmethod
    def filter_by_color(items, color):
        for p in items:
            if p.color == color:
                yield p

    @staticmethod
    def filter_by_size(items, size):
        for p in items:
            if p.size == size:
                yield p

    @staticmethod
    def filter_by_size_and_color(items, color, size):
        for p in items:
            if p.size == size and p.color == color:
                yield p


# below classes demonstrate, how we can implement ocp for ProductFilter class
class Specification:
    """This is base class for specifying filter specification"""
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)


class Filter:
    """This is base class for creating different type of filters"""
    @staticmethod
    def filter(items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    @staticmethod
    def filter(items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == "__main__":
    apple = Product("apple", Color.GREEN, Size.SMALL)
    tree = Product("tree", Color.GREEN, Size.LARGE)
    house = Product("house", Color.BLUE, Size.LARGE)
    products = [apple, tree, house]

    print("filter green color products by older approach:")
    for p in ProductFilter.filter_by_color(products, Color.GREEN):
        print(f" - {p.name}")

    print("filter green color products by new approach:")
    green_spec = ColorSpecification(Color.GREEN)
    for p in BetterFilter.filter(products, green_spec):
        print(f" - {p.name}")

    print("filter large products by new approach:")
    large_spec = SizeSpecification(Size.LARGE)
    for p in BetterFilter.filter(products, large_spec):
        print(f"- {p.name}")

    print("filter large and blue products by new approach:")
    # blue_and_large_spec =
    # AndSpecification(ColorSpecification(Color.BLUE), large_spec)
    blue_and_large_spec = ColorSpecification(Color.BLUE) & large_spec
    for p in BetterFilter.filter(products, blue_and_large_spec):
        print(f"- {p.name}")
