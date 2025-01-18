# Standard Library
import types

# From apps
from utils.point import Point

content = types.SimpleNamespace()
content.ROBOT = "@"
content.BOX = "O"
content.WALL = "#"
content.EMPTY = "."

move = types.SimpleNamespace()
move.UP = "^"
move.DOWN = "v"
move.LEFT = "<"
move.RIGHT = ">"


class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        map = []
        directions = []
        for line in file_content:
            if len(line) == 0:
                continue

            line_chars = list(line)

            if line.startswith(content.WALL):
                map.append(line_chars)
                continue

            directions.extend(line_chars)

        end_map = cls.process_directions(map=map, directions=directions)

        return cls.calculate_value(map=end_map)

    @classmethod
    def process_directions(cls, map: list[list[str]], directions: list[str]) -> list[list[str]]:
        robot_progress = map
        for direction in directions:
            robot_progress = cls.move_robot(direction=direction, map=robot_progress)
            continue

        return robot_progress

    @classmethod
    def move_robot(cls, map: list[list[str]], direction: str) -> list[list[str]]:
        new_map = map.copy()
        robot_location = cls.find_robot(map=new_map)
        next_location = cls.get_next_location(robot_location, direction)

        if content.WALL == new_map[next_location.y][next_location.x]:
            return new_map
        if content.EMPTY == new_map[next_location.y][next_location.x]:
            new_map[robot_location.y][robot_location.x] = content.EMPTY
            new_map[next_location.y][next_location.x] = content.ROBOT
            return new_map
        if content.BOX == new_map[next_location.y][next_location.x]:
            can_move, next_free_space = cls.check_movement(
                direction=direction, map=new_map, robot_location=robot_location
            )
            if can_move and next_free_space:
                new_map[next_free_space.y][next_free_space.x] = content.BOX
                new_map[next_location.y][next_location.x] = content.ROBOT
                new_map[robot_location.y][robot_location.x] = content.EMPTY
            return new_map
        return new_map

    @classmethod
    def find_robot(cls, map: list[list[str]]) -> Point:
        for row in range(len(map)):
            for col in range(len(map[row])):
                if content.ROBOT == map[row][col]:
                    return Point(x=col, y=row)
        raise ValueError("🚨 Robot not present in map 🚨")

    @classmethod
    def calculate_value(cls, map: list[list[str]]) -> int:
        total = 0
        for row in range(len(map)):
            for col in range(len(map[row])):
                if content.BOX == map[row][col]:
                    box_value = row * 100 + col
                    total = total + box_value
        return total

    @classmethod
    def get_next_location(cls, robot: Point, direction: str) -> Point:
        match direction:
            case move.UP:
                return Point(robot.x, robot.y - 1)
            case move.DOWN:
                return Point(robot.x, robot.y + 1)
            case move.LEFT:
                return Point(robot.x - 1, robot.y)
            case move.RIGHT:
                return Point(robot.x + 1, robot.y)
            case _:
                raise ValueError("Unexpected direction encountered: {direction}".format(direction=direction))

    @classmethod
    def check_movement(cls, direction: str, map: list[list[str]], robot_location: Point) -> tuple[bool, Point | None]:
        match direction:
            case move.UP:
                row = robot_location.y
                while row >= 0:
                    if content.WALL == map[row][robot_location.x]:
                        return (False, None)
                    if content.EMPTY == map[row][robot_location.x]:
                        return (True, Point(robot_location.x, row))
                    row = row - 1
                raise ValueError("Loop ran to completion")
            case move.DOWN:
                row = robot_location.y
                while row < len(map):
                    if content.WALL == map[row][robot_location.x]:
                        return (False, None)
                    if content.EMPTY == map[row][robot_location.x]:
                        return (True, Point(robot_location.x, row))
                    row = row + 1
                raise ValueError("Loop ran to completion")
            case move.LEFT:
                col = robot_location.x
                while col >= 0:
                    if content.WALL == map[robot_location.y][col]:
                        return (False, None)
                    if content.EMPTY == map[robot_location.y][col]:
                        return (True, Point(col, robot_location.y))
                    col = col - 1
                raise ValueError("Loop ran to completion")
            case move.RIGHT:
                col = robot_location.x
                while col < len(map[0]):
                    if content.WALL == map[robot_location.y][col]:
                        return (False, None)
                    if content.EMPTY == map[robot_location.y][col]:
                        return (True, Point(col, robot_location.y))
                    col = col + 1
                raise ValueError("Loop ran to completion")
            case _:
                raise ValueError("Unexpected direction encountered: {direction}".format(direction=direction))
        return (False, None)
