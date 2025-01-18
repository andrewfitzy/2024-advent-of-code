# Standard Library
import types
from collections import deque

# From apps
from utils.point import Point

content = types.SimpleNamespace()
content.ROBOT = "@"
content.BOX = "O"
content.BOX_LEFT = "["
content.BOX_RIGHT = "]"
content.WALL = "#"
content.EMPTY = "."

move = types.SimpleNamespace()
move.UP = "^"
move.DOWN = "v"
move.LEFT = "<"
move.RIGHT = ">"


class Task02:
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

        doubled_map = cls.double_map(map=map)

        end_map = cls.process_directions(map=doubled_map, directions=directions)

        return cls.calculate_value(map=end_map)

    @classmethod
    def double_map(cls, map: list[list[str]]) -> list[list[str]]:
        doubled_map = []
        for row in range(len(map)):
            doubled_row = []
            for col in range(len(map[row])):
                value = map[row][col]
                match value:
                    case content.WALL:
                        doubled_row.append(content.WALL)
                        doubled_row.append(content.WALL)
                    case content.EMPTY:
                        doubled_row.append(content.EMPTY)
                        doubled_row.append(content.EMPTY)
                    case content.ROBOT:
                        doubled_row.append(content.ROBOT)
                        doubled_row.append(content.EMPTY)
                    case content.BOX:
                        doubled_row.append(content.BOX_LEFT)
                        doubled_row.append(content.BOX_RIGHT)
                    case _:
                        raise ValueError("Unexpected identifier encountered: {value}".format(value=value))
            doubled_map.append(doubled_row)
        return doubled_map

    @classmethod
    def process_directions(cls, map: list[list[str]], directions: list[str]) -> list[list[str]]:
        robot_progress = map
        for direction in directions:
            robot_progress = cls.move_robot(direction=direction, map=robot_progress)
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
        if (
            content.BOX_LEFT == new_map[next_location.y][next_location.x]
            or content.BOX_RIGHT == new_map[next_location.y][next_location.x]
        ):
            if move.LEFT == direction:
                movements = cls.shuffle_left(map=new_map, robot_location=robot_location)
            if move.RIGHT == direction:
                movements = cls.shuffle_right(map=new_map, robot_location=robot_location)
            if move.UP == direction:
                movements = cls.shuffle_up(map=new_map, robot_location=robot_location)
            if move.DOWN == direction:
                movements = cls.shuffle_down(map=new_map, robot_location=robot_location)
            # apply changes here
            if len(movements) > 0:
                for movement in movements:
                    new_map[movement.y][movement.x] = movements[movement]

                new_map[robot_location.y][robot_location.x] = content.EMPTY
                new_map[next_location.y][next_location.x] = content.ROBOT
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
                if content.BOX_LEFT == map[row][col]:
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
    def shuffle_left(cls, map: list[list[str]], robot_location: Point) -> dict[Point, str]:
        movements = {}

        col = robot_location.x
        while col >= 0:
            if content.WALL == map[robot_location.y][col]:
                return {}

            if content.EMPTY == map[robot_location.y][col]:
                free_space = Point(col, robot_location.y)
                break

            col = col - 1

        for index in range(free_space.x, robot_location.x):
            movements[Point(x=index, y=robot_location.y)] = map[robot_location.y][index + 1]

        return movements

    @classmethod
    def shuffle_right(cls, map: list[list[str]], robot_location: Point) -> dict[Point, str]:
        movements = {}

        col = robot_location.x
        while col < len(map[0]):
            if content.WALL == map[robot_location.y][col]:
                return {}

            if content.EMPTY == map[robot_location.y][col]:
                free_space = Point(col, robot_location.y)
                break

            col = col + 1

        for index in range(robot_location.x + 1, free_space.x + 1):
            movements[Point(x=index, y=robot_location.y)] = map[robot_location.y][index - 1]

        return movements

    @classmethod
    def shuffle_up(cls, map: list[list[str]], robot_location: Point) -> dict[Point, str]:
        step_queue: deque[Point] = deque()
        step_queue.append(robot_location)

        movements = {}

        while len(step_queue) > 0:
            point = step_queue.popleft()
            if content.WALL == map[point.y - 1][point.x]:
                return {}
            if content.BOX_RIGHT == map[point.y - 1][point.x]:
                bottom_left = Point(point.x - 1, point.y - 1)
                bottom_right = Point(point.x, point.y - 1)
                top_left = Point(x=point.x - 1, y=point.y - 2)
                top_right = Point(x=point.x, y=point.y - 2)
                step_queue.append(bottom_left)
                step_queue.append(bottom_right)

                if bottom_left not in movements:
                    movements[bottom_left] = content.EMPTY
                if bottom_right not in movements:
                    movements[bottom_right] = content.EMPTY
                if top_left not in movements:
                    movements[top_left] = map[point.y - 1][point.x - 1]
                if top_right not in movements:
                    movements[top_right] = map[point.y - 1][point.x]
            if content.BOX_LEFT == map[point.y - 1][point.x]:
                bottom_left = Point(point.x, point.y - 1)
                bottom_right = Point(point.x + 1, point.y - 1)
                top_left = Point(x=point.x, y=point.y - 2)
                top_right = Point(x=point.x + 1, y=point.y - 2)
                step_queue.append(bottom_left)
                step_queue.append(bottom_right)

                if bottom_left not in movements:
                    movements[bottom_left] = content.EMPTY
                if bottom_right not in movements:
                    movements[bottom_right] = content.EMPTY
                if top_left not in movements:
                    movements[top_left] = map[point.y - 1][point.x]
                if top_right not in movements:
                    movements[top_right] = map[point.y - 1][point.x + 1]

        return movements

    @classmethod
    def shuffle_down(cls, map: list[list[str]], robot_location: Point) -> dict[Point, str]:
        step_queue: deque[Point] = deque()
        step_queue.append(robot_location)

        movements = {}

        while len(step_queue) > 0:
            point = step_queue.popleft()
            if content.WALL == map[point.y + 1][point.x]:
                return {}
            if content.BOX_RIGHT == map[point.y + 1][point.x]:
                top_left = Point(point.x - 1, point.y + 1)
                top_right = Point(point.x, point.y + 1)
                bottom_left = Point(x=point.x - 1, y=point.y + 2)
                bottom_right = Point(x=point.x, y=point.y + 2)
                step_queue.append(top_left)
                step_queue.append(top_right)

                if bottom_left not in movements:
                    movements[bottom_left] = map[point.y + 1][point.x - 1]
                if bottom_right not in movements:
                    movements[bottom_right] = map[point.y + 1][point.x]
                if top_left not in movements:
                    movements[top_left] = content.EMPTY
                if top_right not in movements:
                    movements[top_right] = content.EMPTY
            if content.BOX_LEFT == map[point.y + 1][point.x]:
                top_left = Point(point.x, point.y + 1)
                top_right = Point(point.x + 1, point.y + 1)
                bottom_left = Point(x=point.x, y=point.y + 2)
                bottom_right = Point(x=point.x + 1, y=point.y + 2)
                step_queue.append(top_left)
                step_queue.append(top_right)

                if bottom_left not in movements:
                    movements[bottom_left] = map[point.y + 1][point.x]
                if bottom_right not in movements:
                    movements[bottom_right] = map[point.y + 1][point.x + 1]
                if top_left not in movements:
                    movements[top_left] = content.EMPTY
                if top_right not in movements:
                    movements[top_right] = content.EMPTY

        return movements
