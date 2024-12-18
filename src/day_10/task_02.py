# Standard Library
from collections import deque

# From apps
from utils.point import Point


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        # read into a 2d array getting all 0s at the same time
        map: list[list[int]] = []
        start_points = []
        row_pointer = 0
        while row_pointer < len(file_content):
            row = []
            column_pointer = 0
            while column_pointer < len(file_content[row_pointer]):
                if file_content[row_pointer][column_pointer] == ".":
                    row.append(-1)
                else:
                    cell_int = int(file_content[row_pointer][column_pointer])
                    row.append(cell_int)
                    if cell_int == 0:
                        start_points.append(Point(x=column_pointer, y=row_pointer))
                column_pointer = column_pointer + 1

            map.append(row)
            row_pointer = row_pointer + 1

        score = 0
        for start_point in start_points:
            destinations = cls.get_routes(start_point, map)
            score = score + len(destinations)

        return score

    @classmethod
    def get_routes(cls, start_point: Point, map: list[list[int]]) -> list[Point]:
        # from point, bfs to find all the 9's that are reachable
        step_queue: deque[Point] = deque()
        step_queue.append(start_point)

        destinations = []

        while len(step_queue) > 0:
            point = step_queue.popleft()
            if map[point.y][point.x] == 9:
                destinations.append(point)
                continue

            moves = cls.get_available_moves(point, map)
            step_queue.extend(moves)

        return destinations

    @classmethod
    def get_available_moves(cls, start_point: Point, map: list[list[int]]) -> list[Point]:
        # check next cell up/down/left/right is equal to the expected next_value
        next_value = map[start_point.y][start_point.x] + 1

        available_moves = []
        if start_point.x - 1 >= 0 and next_value == map[start_point.y][start_point.x - 1]:
            # can move left
            available_moves.append(Point(start_point.x - 1, start_point.y))

        if start_point.y - 1 >= 0 and next_value == map[start_point.y - 1][start_point.x]:
            # can move up
            available_moves.append(Point(start_point.x, start_point.y - 1))

        if start_point.x + 1 < len(map[start_point.y]) and next_value == map[start_point.y][start_point.x + 1]:
            # can move right
            available_moves.append(Point(start_point.x + 1, start_point.y))

        if start_point.y + 1 < len(map) and next_value == map[start_point.y + 1][start_point.x]:
            # can move down
            available_moves.append(Point(start_point.x, start_point.y + 1))

        return available_moves
