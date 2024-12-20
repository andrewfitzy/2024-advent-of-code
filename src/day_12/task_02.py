# Standard Library
from collections import deque

# From apps
from utils.point import Point


class Task02:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        grid = []
        for line in file_content:
            grid.append(list(line))

        regions = cls.get_regions(grid)

        total_cost = 0
        for content, region_list in regions.items():
            for region in region_list:
                cost = cls.get_region_cost(content, region, grid)
                print(f"{content} {cost}")
                total_cost = total_cost + cost

        return total_cost

    @classmethod
    def get_regions(cls, grid: list[list[str]]) -> dict[str, list[set[Point]]]:
        regions: dict[str, list[set[Point]]] = {}
        seen = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                start_point = Point(col, row)
                if start_point not in seen:
                    content = grid[start_point.y][start_point.x]

                    # get the points from here
                    region = cls.get_region(start_point, grid)
                    seen.update(region)

                    existing_regions = regions.get(content, [])
                    existing_regions.append(region)
                    regions[content] = existing_regions

        return regions

    @classmethod
    def get_region(cls, start: Point, grid: list[list[str]]) -> set[Point]:
        # from point, bfs to find all the items in the region
        step_queue: deque[Point] = deque()
        step_queue.append(start)

        seen: set[Point] = set()
        seen.add(start)

        region = set()
        region.add(start)
        content = grid[start.y][start.x]
        while len(step_queue) > 0:
            point = step_queue.popleft()

            moves = cls.get_available_moves(point, content, grid)

            for move in moves:
                if move in seen:
                    continue
                if grid[move.y][move.x] == content:
                    region.add(move)
                seen.add(move)
                step_queue.append(move)

        return region

    @classmethod
    def get_available_moves(cls, start_point: Point, content: str, grid: list[list[str]]) -> list[Point]:
        # check next cell up/down/left/right is equal to the expected next_value
        available_moves = []
        if start_point.x - 1 >= 0 and content == grid[start_point.y][start_point.x - 1]:
            # can move left
            available_moves.append(Point(start_point.x - 1, start_point.y))

        if start_point.y - 1 >= 0 and content == grid[start_point.y - 1][start_point.x]:
            # can move up
            available_moves.append(Point(start_point.x, start_point.y - 1))

        if start_point.x + 1 < len(grid[start_point.y]) and content == grid[start_point.y][start_point.x + 1]:
            # can move right
            available_moves.append(Point(start_point.x + 1, start_point.y))

        if start_point.y + 1 < len(grid) and content == grid[start_point.y + 1][start_point.x]:
            # can move down
            available_moves.append(Point(start_point.x, start_point.y + 1))

        return available_moves

    @classmethod
    def get_region_cost(cls, content: str, region: set[Point], grid: list[list[str]]) -> int:
        sides = 1

        # Need to calculate sides here, will return to this one day when I can work out how this is done :()

        cost = sides * len(region)

        return cost
