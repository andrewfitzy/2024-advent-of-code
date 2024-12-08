# Standard Library
import math


def get_manhattan_distance(this_x: int, this_y, other_x: int, other_y: int) -> int:
    return int(math.fabs(other_x - this_x) + math.fabs(other_y - this_y))
