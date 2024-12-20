# Standard Library
import math
import re

# From apps
from utils.point import Point


class Task01:
    @classmethod
    def solve(cls, width: int, height: int, file_content: list[str]) -> int:
        pattern = re.compile("p=(-?\\d+),(-?\\d+) v=(-?\\d+),(-?\\d+)")
        robots = []
        for line in file_content:
            mul_instructions = pattern.findall(line)
            for instruction in mul_instructions:
                position = Point(int(instruction[0]), int(instruction[1]))
                velocity = Point(int(instruction[2]), int(instruction[3]))
                robots.append((position, velocity))

        for count in range(100):
            robots = cls.move_robots(width=width, height=height, robots=robots)

        return cls.calculate_safety_factor(width=width, height=height, robots=robots)

    @classmethod
    def move_robots(cls, width: int, height: int, robots: list[tuple[Point, Point]]) -> list[tuple[Point, Point]]:
        new_positions = []
        for robot in robots:
            current_position = robot[0]
            movement = robot[1]
            new_x = (current_position.x + movement.x) % width
            new_y = (current_position.y + movement.y) % height
            new_position = Point(x=new_x, y=new_y)
            new_positions.append((new_position, movement))

        return new_positions

    @classmethod
    def calculate_safety_factor(cls, width: int, height: int, robots: list[tuple[Point, Point]]) -> int:
        mid_x = math.floor(width / 2)
        mid_y = math.floor(height / 2)

        top_left = 0
        top_right = 0
        bottom_left = 0
        bottom_right = 0
        for robot in robots:
            if robot[0].is_in_bounds(start_x=0, start_y=0, width=mid_x, height=mid_y):
                top_left = top_left + 1

            if robot[0].is_in_bounds(start_x=mid_x + 1, start_y=0, width=mid_x, height=mid_y):
                top_right = top_right + 1

            if robot[0].is_in_bounds(start_x=0, start_y=mid_y + 1, width=mid_x, height=mid_y):
                bottom_left = bottom_left + 1

            if robot[0].is_in_bounds(start_x=mid_x + 1, start_y=mid_y + 1, width=mid_x, height=mid_y):
                bottom_right = bottom_right + 1
        safety_factor = top_left * top_right * bottom_left * bottom_right
        return safety_factor
