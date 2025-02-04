# Standard Library
import types
from collections import deque

# From apps
from utils.distance import get_manhattan_distance
from utils.point import Point

content = types.SimpleNamespace()
content.START = "S"
content.END = "E"
content.WALL = "#"
content.SPACE = "."

MASK_LENGTH: int = 20


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        maze: list[list[str]] = []
        for line in file_content:
            maze.append(list(line))

        for row in range(len(maze)):
            for col in range(len(maze[row])):
                if content.START == maze[row][col]:
                    start = Point(col, row)
                if content.END == maze[row][col]:
                    end = Point(col, row)

        path = cls.get_path(start=start, end=end, map=maze)

        cheats = cls.get_cheats(path, map=maze)

        acceptable_cheats = 0
        for key, value in cheats.items():
            if value >= 100:
                acceptable_cheats = acceptable_cheats + 1

        return acceptable_cheats

    @classmethod
    def get_path(cls, start: Point, end: Point, map: list[list[str]]) -> list[Point]:
        step_queue: deque[Point] = deque()
        step_queue.append(start)

        path = []
        seen = set()
        while len(step_queue) > 0:
            point = step_queue.popleft()
            if point in seen:
                continue
            seen.add(point)

            path.append(point)
            if content.END == map[point.y][point.x]:
                break

            moves = cls.get_available_moves(point=point, map=map)
            step_queue.extend(moves)

        return path

    @classmethod
    def get_available_moves(cls, point: Point, map: list[list[str]]) -> list[Point]:
        available_moves = []
        if point.x - 1 >= 0 and content.WALL != map[point.y][point.x - 1]:
            # can move left
            available_moves.append(Point(point.x - 1, point.y))

        if point.y - 1 >= 0 and content.WALL != map[point.y - 1][point.x]:
            # can move up
            available_moves.append(Point(point.x, point.y - 1))

        if point.x + 1 < len(map[point.y]) and content.WALL != map[point.y][point.x + 1]:
            # can move right
            available_moves.append(Point(point.x + 1, point.y))

        if point.y + 1 < len(map) and content.WALL != map[point.y + 1][point.x]:
            # can move down
            available_moves.append(Point(point.x, point.y + 1))

        return available_moves

    @classmethod
    def get_cheats(cls, path: list[Point], map: list[list[str]]) -> dict[tuple[Point, Point], int]:
        position_lookup: dict[Point, int] = dict()
        for index in range(len(path)):
            position_lookup[path[index]] = index

        mask = cls.get_mask(mask_length=MASK_LENGTH)
        cheat_costs: dict[tuple[Point, Point], int] = {}
        for point in path:
            cheat_moves = cls.get_cheat_moves(point=point, mask=mask, map=map)
            for target in cheat_moves:
                start_index = position_lookup[point]
                end_index = position_lookup[target]
                cheat_length = get_manhattan_distance(point.x, point.y, target.x, target.y)
                cost = end_index - start_index - cheat_length

                if cost > 1:  # negative value means going backwards, 1 means moving to next position
                    cheat_costs[(point, target)] = cost
        return cheat_costs

    @classmethod
    def get_cheat_moves(cls, point: Point, mask: set[Point], map: list[list[str]]) -> set[Point]:
        target_content = {content.SPACE, content.END}
        cheat_moves = set()

        for mask_point in mask:
            target_x = point.x + mask_point.x
            target_y = point.y + mask_point.y
            if (
                target_x >= 0
                and target_y >= 0
                and target_x < len(map[point.y])
                and target_y < len(map)
                and map[target_y][target_x] in target_content
            ):
                cheat_moves.add(Point(target_x, target_y))
        return cheat_moves

    @classmethod
    def get_mask(cls, mask_length: int) -> set[Point]:
        # get a diamond of points around a point
        mask_points = set()
        for y in range(-mask_length, mask_length + 1, 1):
            offset = mask_length - abs(y)
            for x in range(-offset, offset + 1, 1):
                mask_points.add(Point(x=x, y=y))
        return mask_points
