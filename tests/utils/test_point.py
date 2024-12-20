# Standard Library
import unittest

# From apps
from utils.point import Point


class TestPoint(unittest.TestCase):
    def test_create(self):
        x = 1
        y = 2

        point = Point(x=x, y=y)

        assert point.x == x
        assert point.y == y

    def test_eq(self):
        x = 1
        y = 2

        this_point = Point(x=x, y=y)
        other_point = Point(x=x, y=y)

        assert this_point.__eq__(other_point)

    def test_hash(self):
        x = 1
        y = 2

        point = Point(x=x, y=y)

        assert point.__hash__() == -3550055125485641917

    def test_str(self):
        x = 1
        y = 2

        point = Point(x=x, y=y)

        assert point.__str__() == "(1, 2)"

    def test_is_in_bounds(self):
        x = 1
        y = 2

        point = Point(x=x, y=y)

        assert point.is_in_bounds(1, 2, 3, 3)

    def test_is_in_bounds_left_of_bounds(self):
        x = 0
        y = 2

        point = Point(x=x, y=y)

        assert not point.is_in_bounds(1, 2, 3, 3)

    def test_is_in_bounds_above_bounds(self):
        x = 1
        y = 0

        point = Point(x=x, y=y)

        assert not point.is_in_bounds(1, 2, 3, 3)

    def test_is_in_bounds_right_of_bounds(self):
        x = 5
        y = 2

        point = Point(x=x, y=y)

        assert not point.is_in_bounds(1, 2, 3, 3)

    def test_is_in_bounds_below_bounds(self):
        x = 1
        y = 6

        point = Point(x=x, y=y)

        assert not point.is_in_bounds(1, 2, 3, 3)
