# Standard Library
import unittest

# From apps
from utils.distance import get_manhattan_distance


class TestDistance(unittest.TestCase):
    def test_get_manhattan_distance_with_movement_NE(self):
        this_x = 10
        this_y = 10
        other_x = 15
        other_y = 15

        output = get_manhattan_distance(this_x, this_y, other_x, other_y)

        assert output == 10

    def test_get_manhattan_distance_with_movement_E(self):
        this_x = 10
        this_y = 10
        other_x = 15
        other_y = 10

        output = get_manhattan_distance(this_x, this_y, other_x, other_y)

        assert output == 5

    def test_get_manhattan_distance_with_movement_SE(self):
        this_x = 10
        this_y = 10
        other_x = 15
        other_y = 5

        output = get_manhattan_distance(this_x, this_y, other_x, other_y)

        assert output == 10

    def test_get_manhattan_distance_with_movement_S(self):
        this_x = 10
        this_y = 10
        other_x = 10
        other_y = 5

        output = get_manhattan_distance(this_x, this_y, other_x, other_y)

        assert output == 5

    def test_get_manhattan_distance_with_movement_SW(self):
        this_x = 10
        this_y = 10
        other_x = 5
        other_y = 5

        output = get_manhattan_distance(this_x, this_y, other_x, other_y)

        assert output == 10

    def test_get_manhattan_distance_with_movement_W(self):
        this_x = 10
        this_y = 10
        other_x = 5
        other_y = 10

        output = get_manhattan_distance(this_x, this_y, other_x, other_y)

        assert output == 5

    def test_get_manhattan_distance_with_movement_NW(self):
        this_x = 10
        this_y = 10
        other_x = 5
        other_y = 15

        output = get_manhattan_distance(this_x, this_y, other_x, other_y)

        assert output == 10

    def test_get_manhattan_distance_with_movement_N(self):
        this_x = 10
        this_y = 10
        other_x = 10
        other_y = 15

        output = get_manhattan_distance(this_x, this_y, other_x, other_y)

        assert output == 5

    def test_get_manhattan_distance_with_movement_NE_and_negative_coords(self):
        this_x = -10
        this_y = -10
        other_x = -5
        other_y = -5

        output = get_manhattan_distance(this_x, this_y, other_x, other_y)

        assert output == 10
