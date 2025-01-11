# From apps
from utils.point import Point

ROBOT = "@"
BOX = "O"
WALL = "#"
EMPTY = "."


class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        map = []
        directions = []
        for line in file_content:
            if len(line) == 0:
                continue

            line_chars = list(line)

            if line.startswith("#"):
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

        if WALL == new_map[next_location.y][next_location.x]:
            return new_map
        if EMPTY == new_map[next_location.y][next_location.x]:
            new_map[robot_location.y][robot_location.x] = EMPTY
            new_map[next_location.y][next_location.x] = ROBOT
            return new_map
        if BOX == new_map[next_location.y][next_location.x]:
            can_move, next_free_space = cls.check_movement(
                direction=direction, map=new_map, robot_location=robot_location
            )
            if can_move and next_free_space:
                new_map[next_free_space.y][next_free_space.x] = BOX
                new_map[next_location.y][next_location.x] = ROBOT
                new_map[robot_location.y][robot_location.x] = EMPTY
            return new_map
        return new_map

    @classmethod
    def find_robot(cls, map: list[list[str]]) -> Point:
        for row in range(len(map)):
            for col in range(len(map[row])):
                if ROBOT == map[row][col]:
                    return Point(x=col, y=row)
        raise ValueError("Robot not present in map")

    @classmethod
    def calculate_value(cls, map: list[list[str]]) -> int:
        total = 0
        for row in range(len(map)):
            for col in range(len(map[row])):
                if BOX == map[row][col]:
                    box_value = row * 100 + col
                    total = total + box_value
        return total

    @classmethod
    def get_next_location(cls, robot: Point, direction: str) -> Point:
        match direction:
            case "^":
                return Point(robot.x, robot.y - 1)
            case "v":
                return Point(robot.x, robot.y + 1)
            case "<":
                return Point(robot.x - 1, robot.y)
            case ">":
                return Point(robot.x + 1, robot.y)
            case _:
                raise ValueError("Unexpected direction encountered")

    @classmethod
    def check_movement(cls, direction: str, map: list[list[str]], robot_location: Point) -> tuple[bool, Point | None]:
        match direction:
            case "^":
                row = robot_location.y
                while row >= 0:
                    if WALL == map[row][robot_location.x]:
                        return (False, None)
                    if EMPTY == map[row][robot_location.x]:
                        return (True, Point(robot_location.x, row))
                    row = row - 1
                raise ValueError("Loop ran to completion")
            case "v":
                row = robot_location.y
                while row < len(map):
                    if WALL == map[row][robot_location.x]:
                        return (False, None)
                    if EMPTY == map[row][robot_location.x]:
                        return (True, Point(robot_location.x, row))
                    row = row + 1
                raise ValueError("Loop ran to completion")
            case "<":
                col = robot_location.x
                while col >= 0:
                    if WALL == map[robot_location.y][col]:
                        return (False, None)
                    if EMPTY == map[robot_location.y][col]:
                        return (True, Point(col, robot_location.y))
                    col = col - 1
                raise ValueError("Loop ran to completion")
            case ">":
                col = robot_location.x
                while col < len(map[0]):
                    if WALL == map[robot_location.y][col]:
                        return (False, None)
                    if EMPTY == map[robot_location.y][col]:
                        return (True, Point(col, robot_location.y))
                    col = col + 1
                raise ValueError("Loop ran to completion")
            case _:
                raise ValueError("Unexpected direction encountered")
        return (False, None)
