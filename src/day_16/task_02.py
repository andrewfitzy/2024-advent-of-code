# Standard Library
import heapq
import types
from dataclasses import dataclass, field

# From apps
from utils.point import Point

content = types.SimpleNamespace()
content.START = "S"
content.END = "E"
content.WALL = "#"
content.SPACE = "."

direction = types.SimpleNamespace()
direction.UP = "^"
direction.DOWN = "v"
direction.LEFT = "<"
direction.RIGHT = ">"


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    direction: str = field(compare=False)
    point: Point = field(compare=False)
    path: set[Point] = field(compare=False)


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

        cost = cls.get_cheapest_path(start=start, end=end, maze=maze)
        paths = cls.get_paths_with_cost(start=start, end=end, cost=cost, maze=maze)

        for path in paths:
            cls.print_map(path, maze)
            print("")

        seen = set()
        for path in paths:
            for point in path:
                seen.add(point)
        print(len(seen))
        return len(seen)

    @classmethod
    def print_map(cls, path, maze: list[list[str]]):
        for row in maze:
            print("".join(row))

        for row_i in range(len(maze)):
            row_str = []
            for col_i in range(len(maze[row_i])):
                if Point(x=col_i, y=row_i) in path:
                    row_str.append("o")
                    continue
                row_str.append(maze[row_i][col_i])
            print("".join(row_str))

    @classmethod
    def get_paths_with_cost(cls, start: Point, end: Point, cost: int, maze: list[list[str]]) -> list[set[Point]]:
        step_queue: list[PrioritizedItem] = []
        heapq.heappush(step_queue, PrioritizedItem(priority=0, direction=direction.RIGHT, point=start, path=set()))

        paths = []
        while len(step_queue) > 0:
            item = heapq.heappop(step_queue)

            point = item.point
            if content.WALL == maze[point.y][point.x]:
                continue
            if content.END == maze[point.y][point.x]:
                item.path.add(point)
                paths.append(item.path)
                continue

            # are we coming back on ourselves?
            if item.point in item.path:
                continue
            # are we now over the max cost?
            if item.priority > cost:
                continue

            moves = cls.get_available_moves(point, item.direction, maze)
            for next_point, next_cost, next_direction in moves:
                new_cost = item.priority + next_cost
                new_path = item.path.copy()
                new_path.add(point)
                heapq.heappush(
                    step_queue,
                    PrioritizedItem(priority=new_cost, direction=next_direction, point=next_point, path=new_path),
                )

        return paths

    @classmethod
    def get_cheapest_path(cls, start: Point, end: Point, maze: list[list[str]]) -> int:
        step_queue: list[PrioritizedItem] = []
        heapq.heappush(step_queue, PrioritizedItem(priority=0, direction=direction.RIGHT, point=start, path=set()))

        seen = {(start, direction.RIGHT)}

        while len(step_queue) > 0:
            item = heapq.heappop(step_queue)
            seen.add((item.point, item.direction))

            point = item.point
            if content.WALL == maze[point.y][point.x]:
                continue
            if content.END == maze[point.y][point.x]:
                return item.priority

            moves = cls.get_available_moves(point, item.direction, maze)
            for next_point, next_cost, next_direction in moves:
                new_cost = item.priority + next_cost

                if (next_point, next_direction) not in seen:
                    heapq.heappush(
                        step_queue,
                        PrioritizedItem(priority=new_cost, direction=next_direction, point=next_point, path=item.path),
                    )

        return -1

    @classmethod
    def get_available_moves(cls, point: Point, facing: str, map: list[list[str]]) -> list[tuple[Point, int, str]]:
        available_moves = []
        if point.x - 1 >= 0 and content.WALL != map[point.y][point.x - 1]:
            # can move left
            left_point = Point(point.x - 1, point.y)
            if direction.LEFT == facing:
                available_moves.append((left_point, 1, direction.LEFT))
            elif direction.RIGHT == facing:
                available_moves.append((left_point, 2001, direction.LEFT))
            else:
                available_moves.append((left_point, 1001, direction.LEFT))
        if point.y - 1 >= 0 and content.WALL != map[point.y - 1][point.x]:
            # can move up
            up_point = Point(point.x, point.y - 1)
            if direction.UP == facing:
                available_moves.append((up_point, 1, direction.UP))
            elif direction.DOWN == facing:
                available_moves.append((up_point, 2001, direction.UP))
            else:
                available_moves.append((up_point, 1001, direction.UP))

        if point.x + 1 < len(map[point.y]) and content.WALL != map[point.y][point.x + 1]:
            # can move right
            right_point = Point(point.x + 1, point.y)
            if direction.RIGHT == facing:
                available_moves.append((right_point, 1, direction.RIGHT))
            elif direction.LEFT == facing:
                available_moves.append((right_point, 2001, direction.RIGHT))
            else:
                available_moves.append((right_point, 1001, direction.RIGHT))

        if point.y + 1 < len(map) and content.WALL != map[point.y + 1][point.x]:
            # can move down
            down_point = Point(point.x, point.y + 1)
            if direction.DOWN == facing:
                available_moves.append((down_point, 1, direction.DOWN))
            elif direction.UP == facing:
                available_moves.append((down_point, 2001, direction.DOWN))
            else:
                available_moves.append((down_point, 1001, direction.DOWN))

        return available_moves
