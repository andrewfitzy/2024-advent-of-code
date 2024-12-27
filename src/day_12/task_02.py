# Standard Library
from collections import deque

# From apps
from utils.point import Point

OFFSET = 1


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
        # first get edge points
        edge_points = cls.get_region_edges(region, grid)

        horizontal_edges = cls.count_horizontal_edges(edge_points)
        vertical_edges = cls.count_vertical_edges(edge_points)

        cost = (horizontal_edges + vertical_edges) * len(region)

        return cost

    @classmethod
    def get_region_edges(cls, region: set[Point], grid: list[list[str]]) -> dict[Point, list[Point]]:
        edges = {}
        for point in region:
            content = grid[point.y][point.x]
            edge_list = []
            # check next cell up/down/left/right is out of bounds or different content
            if point.x - 1 < 0 or content != grid[point.y][point.x - 1]:
                # can move left
                edge_list.append(Point(point.x - OFFSET, point.y))

            if point.y - 1 < 0 or content != grid[point.y - 1][point.x]:
                # can move up
                edge_list.append(Point(point.x, point.y - OFFSET))

            if point.x + 1 >= len(grid[point.y]) or content != grid[point.y][point.x + 1]:
                # can move right
                edge_list.append(Point(point.x + OFFSET, point.y))

            if point.y + 1 >= len(grid) or content != grid[point.y + 1][point.x]:
                # can move down
                edge_list.append(Point(point.x, point.y + OFFSET))

            # ignore if the point is central to the shape
            if len(edge_list) > 0:
                edges[point] = edge_list
        return edges

    @classmethod
    def count_horizontal_edges(cls, edges: dict[Point, list[Point]]) -> int:
        total_top_edges = 0
        total_bottom_edges = 0
        min_x = -1
        min_y = -1
        max_x = 0
        max_y = 0
        for point in edges:
            if point.x < min_x or min_x == -1:
                min_x = point.x
            if point.y < min_y or min_y == -1:
                min_y = point.y
            if point.x > max_x:
                max_x = point.x
            if point.y > max_y:
                max_y = point.y
        # add one as will not process last x or y otherwise
        max_x = max_x + 1
        max_y = max_y + 1

        for row in range(min_y, max_y):
            top_count = 0
            bottom_count = 0
            last_top = -2
            last_bottom = -2
            for col in range(min_x, max_x):
                current_point = Point(col, row)
                if current_point not in edges:
                    continue
                point_edges = edges[current_point]
                above_edge = Point(current_point.x, current_point.y - OFFSET)
                below_edge = Point(current_point.x, current_point.y + OFFSET)

                if above_edge in point_edges:
                    if last_top == col - 1:
                        last_top = col
                    else:
                        last_top = col
                        top_count = top_count + 1

                if below_edge in point_edges:
                    if last_bottom == col - 1:
                        last_bottom = col
                    else:
                        last_bottom = col
                        bottom_count = bottom_count + 1

            total_top_edges = total_top_edges + top_count
            total_bottom_edges = total_bottom_edges + bottom_count

        return total_top_edges + total_bottom_edges

    @classmethod
    def count_vertical_edges(cls, edges: dict[Point, list[Point]]) -> int:
        total_left_edges = 0
        total_right_edges = 0
        min_x = -1
        min_y = -1
        max_x = 0
        max_y = 0
        for point in edges:
            if point.x < min_x or min_x == -1:
                min_x = point.x
            if point.y < min_y or min_y == -1:
                min_y = point.y
            if point.x > max_x:
                max_x = point.x
            if point.y > max_y:
                max_y = point.y
        # add one as will not process last x or y otherwise
        max_x = max_x + 1
        max_y = max_y + 1

        for col in range(min_x, max_x):
            left_count = 0
            right_count = 0
            last_left = -2
            last_right = -2
            for row in range(min_y, max_y):
                current_point = Point(col, row)
                if current_point not in edges:
                    continue
                point_edges = edges[current_point]
                left_edge = Point(current_point.x - OFFSET, current_point.y)
                right_edge = Point(current_point.x + OFFSET, current_point.y)

                if left_edge in point_edges:
                    if last_left == row - 1:
                        last_left = row
                    else:
                        last_left = row
                        left_count = left_count + 1

                if right_edge in point_edges:
                    if last_right == row - 1:
                        last_right = row
                    else:
                        last_right = row
                        right_count = right_count + 1

            total_left_edges = total_left_edges + left_count
            total_right_edges = total_right_edges + right_count

        return total_left_edges + total_right_edges
