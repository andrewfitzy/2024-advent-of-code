# Standard Library
import math
from collections import deque

# From apps
from utils.point import Point


class Task02:
    @classmethod
    def solve(cls, file_content: list[str], max_dimension: int) -> str:
        # Process the input
        byte_list = []
        for line in file_content:
            parts = line.split(",")
            byte = Point(int(parts[0]), int(parts[1]))
            byte_list.append(byte)

        start_pointer = 0
        end_pointer = len(byte_list)

        # protection against infinite loops, break if this doesn't change
        last_mid = -100

        while start_pointer <= end_pointer:
            mid_pointer = math.floor((start_pointer + end_pointer) / 2)

            dropped_bytes = byte_list[0:mid_pointer]
            current_grid = cls.get_current_grid(max_dimension, dropped_bytes)
            shortest_route = cls.shortest_route(
                start=Point(0, 0), end=Point(max_dimension, max_dimension), grid=current_grid
            )

            if len(shortest_route) == 0:
                end_pointer = mid_pointer
            else:
                start_pointer = mid_pointer

            # protection against infinite loops, break if this doesn't change
            if last_mid == mid_pointer:
                break
            else:
                last_mid = mid_pointer

        blocking_point = byte_list[start_pointer]
        return str(blocking_point.x) + "," + str(blocking_point.y)

    @classmethod
    def get_current_grid(cls, max_dimension: int, dropped_bytes: list[Point]) -> list[list[str]]:
        # copy?
        grid: list[list[str]] = []
        for index in range(max_dimension + 1):
            grid.append(["."] * (max_dimension + 1))

        for byte in dropped_bytes:
            grid[byte.y][byte.x] = "#"
        return grid

    @classmethod
    def shortest_route(cls, start: Point, end: Point, grid: list[list[str]]) -> list[Point]:
        # from point, bfs to find the shortest route
        step_queue: deque[tuple[Point, set[Point]]] = deque()
        start_route: set[Point] = set()
        start_route.add(start)
        step_queue.append((start, start_route))

        seen: set[Point] = set()
        seen.add(start)

        shortest_route: list[Point] = []
        while len(step_queue) > 0:
            point, route = step_queue.popleft()

            moves = cls.get_available_moves(point, grid)

            for move in moves:
                tmp_route = set(route)
                if move in seen:
                    continue
                if move == end:
                    tmp_route.add(move)
                    if len(shortest_route) == 0 or len(tmp_route) < len(shortest_route):
                        shortest_route = list(tmp_route)
                seen.add(move)
                tmp_route.add(move)
                step_queue.append((move, tmp_route))
        return shortest_route

    @classmethod
    def get_available_moves(cls, start_point: Point, grid: list[list[str]]) -> list[Point]:
        # check next cell up/down/left/right is equal to the expected next_value

        available_moves = []
        if start_point.x - 1 >= 0 and "." == grid[start_point.y][start_point.x - 1]:
            # can move left
            available_moves.append(Point(start_point.x - 1, start_point.y))

        if start_point.y - 1 >= 0 and "." == grid[start_point.y - 1][start_point.x]:
            # can move up
            available_moves.append(Point(start_point.x, start_point.y - 1))

        if start_point.x + 1 < len(grid[start_point.y]) and "." == grid[start_point.y][start_point.x + 1]:
            # can move right
            available_moves.append(Point(start_point.x + 1, start_point.y))

        if start_point.y + 1 < len(grid) and "." == grid[start_point.y + 1][start_point.x]:
            # can move down
            available_moves.append(Point(start_point.x, start_point.y + 1))

        return available_moves
