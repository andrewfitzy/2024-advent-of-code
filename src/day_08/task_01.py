# Standard Library
from itertools import combinations

# From apps
from utils.point import Point


class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        map = []
        for line in file_content:
            map.append(list(line))

        locations_of_pairs = cls.get_antenna_pairs(map)
        # [
        #  (point(1,1),point(2,2)),
        #  (point(1,1),point(2,2)),
        #  (point(1,1),point(2,2)),
        # ]

        antinodes = set()
        for point_01, point_02 in locations_of_pairs:
            (antinode_01, antinode_02) = cls.get_antinodes(point_01, point_02)

            antinodes.add(antinode_01)
            antinodes.add(antinode_02)

        # trim antinodes outside of bounds
        antinodes_in_bounds = []
        for point in antinodes:
            if point.is_in_bounds(0, 0, len(map[0]), len(map)):
                antinodes_in_bounds.append(point)

        return len(antinodes_in_bounds)

    @classmethod
    def get_antenna_pairs(cls, map: list[list[str]]) -> list[tuple[Point, Point]]:
        antenna_pairs = []

        # build a dict of all populated squares
        antennas: dict[str, list[Point]] = {}

        for x in range(len(map[0])):
            for y in range(len(map)):
                content = map[y][x]
                if content != ".":
                    location_list = antennas.get(content, list())
                    location_list.append(Point(x, y))
                    antennas[content] = location_list

        for key, value in antennas.items():
            new_combos = list(combinations(value, 2))
            antenna_pairs.extend(new_combos)

        return antenna_pairs

    @classmethod
    def get_antinodes(cls, point_01: Point, point_02: Point) -> tuple[Point, Point]:
        dx = point_01.x - point_02.x
        dy = point_01.y - point_02.y

        antinode01 = Point(point_01.x + dx, point_01.y + dy)
        antinode02 = Point(point_02.x - dx, point_02.y - dy)
        if (
            antinode01.x == point_02.x
            and antinode01.y == point_02.y
            and antinode02.x == point_01.x
            and antinode02.y == point_01.y
        ):
            antinode01 = Point(point_01.x - dx, point_01.y - dy)
            antinode02 = Point(point_02.x + dx, point_02.y + dy)

        return (antinode01, antinode02)
