# Standard Library

# Standard Library
import re

# From apps
from utils.point import Point


class Task02:
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

        seconds = 0
        while True:
            seconds = seconds + 1
            robots = cls.move_robots(width=width, height=height, robots=robots)
            if cls.has_clashing_robots(robots=robots):
                continue
            cls.print_space(width=width, height=height, robots=robots)
            break

        return seconds

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
    def has_clashing_robots(cls, robots: list[tuple[Point, Point]]) -> bool:
        has_clashing_robots = False

        robot_set = set()
        for robot in robots:
            if robot[0] in robot_set:
                has_clashing_robots = True
                break
            robot_set.add(robot[0])

        return has_clashing_robots

    @classmethod
    def print_space(cls, width: int, height: int, robots: list[tuple[Point, Point]]):
        grid: list[list[str]] = []
        for index in range(height):
            grid.append(["."] * width)

        for robot in robots:
            content = grid[robot[0].y][robot[0].x]
            if content == ".":
                grid[robot[0].y][robot[0].x] = str(1)
                continue
            grid[robot[0].y][robot[0].x] = str(int(content) + 1)

        for row in grid:
            print(" ".join(row))
