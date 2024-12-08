# Standard Library
from itertools import combinations

# From apps
from utils.point import Point


class Task02:
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
            tmp_antinodes = cls.get_antinodes(point_01, point_02, len(map[0]), len(map))
            for tmp_antinode in tmp_antinodes:
                antinodes.add(tmp_antinode)

        return len(antinodes)

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
    def get_antinodes(cls, point_01: Point, point_02: Point, width, height) -> set[Point]:
        dx = point_01.x - point_02.x
        dy = point_01.y - point_02.y

        antinodes = set()
        antinodes.add(point_01)
        antinodes.add(point_02)

        next_node_01 = point_01
        next_node_02 = point_02

        done = False
        while not done:
            antinode01 = Point(next_node_01.x + dx, next_node_01.y + dy)
            antinode02 = Point(next_node_02.x - dx, next_node_02.y - dy)

            added = False
            if antinode01.is_in_bounds(0, 0, width, height):
                antinodes.add(antinode01)
                next_node_01 = antinode01
                added = True

            if antinode02.is_in_bounds(0, 0, width, height):
                antinodes.add(antinode02)
                next_node_02 = antinode02
                added = True

            done = not added

        return antinodes
