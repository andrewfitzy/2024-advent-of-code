# Standard Library
from enum import Enum

# From apps
from utils.point import Point


class Move(Enum):
    UP = Point(x=0, y=-1)
    DOWN = Point(x=0, y=1)
    LEFT = Point(x=-1, y=0)
    RIGHT = Point(x=1, y=0)

    def __init__(self, next_step: Point):
        self.next_step = next_step


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        map = []
        row_pointer = 0
        for line in file_content:
            map.append(list(line))
            column = line.find("^")
            if column > -1:
                guard_start = Point(x=column, y=row_pointer)

            row_pointer = row_pointer + 1

        visited_locations = cls.walk_through_map(guard_start, map)

        blocking_spaces = 0
        for location in visited_locations:
            if cls.is_a_looping_space(guard_start, location, map):
                blocking_spaces = blocking_spaces + 1

        return blocking_spaces

    @classmethod
    def walk_through_map(cls, guard_start: Point, map: list[list[str]]) -> set[Point]:
        visited = set()
        visited.add(guard_start)
        complete = False
        current = guard_start
        direction = Move.UP
        while not complete:
            if (
                current.x + direction.next_step.x == len(map[0])
                or current.y + direction.next_step.y == len(map)
                or current.x + direction.next_step.x == -1
                or current.y + direction.next_step.y == -1
            ):
                complete = True
                continue

            if map[current.y + direction.next_step.y][current.x + direction.next_step.x] == "#":
                direction = cls.turn_right(direction)
                continue

            current = Point(x=current.x + direction.next_step.x, y=current.y + direction.next_step.y)
            visited.add(current)

        return visited

    @classmethod
    def is_a_looping_space(cls, guard_start: Point, space: Point, map: list[list[str]]) -> bool:
        visited = set()

        complete = False
        current = guard_start
        direction = Move.UP
        temp_map = []
        for line in map:
            temp_map.append(line.copy())

        temp_map[space.y][space.x] = "#"

        looping = False
        while not complete:
            if (
                current.x + direction.next_step.x == len(temp_map[0])
                or current.y + direction.next_step.y == len(temp_map)
                or current.x + direction.next_step.x == -1
                or current.y + direction.next_step.y == -1
            ):
                complete = True
                continue

            if temp_map[current.y + direction.next_step.y][current.x + direction.next_step.x] == "#":
                direction = cls.turn_right(direction)
                continue

            current = Point(x=current.x + direction.next_step.x, y=current.y + direction.next_step.y)

            if (current, direction) in visited:
                complete = True
                looping = True
                continue

            visited.add((current, direction))

        return looping

    @classmethod
    def turn_right(cls, current_direction: Move) -> Move:
        if current_direction == Move.UP:
            return Move.RIGHT
        if current_direction == Move.RIGHT:
            return Move.DOWN
        if current_direction == Move.DOWN:
            return Move.LEFT
        return Move.UP
