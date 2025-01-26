# Standard Library
import itertools
import types
from collections import deque

# From apps
from utils.point import Point

move = types.SimpleNamespace()
move.UP = "^"
move.DOWN = "v"
move.LEFT = "<"
move.RIGHT = ">"

content = types.SimpleNamespace()
content.ACTIVATE = "A"

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

keypad = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["", "0", "A"]]


#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

directional_pad = [
    ["", "^", "A"],
    ["<", "v", ">"],
]

number_of_robots = 2


class Task01:
    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        keypad_transitions = cls.precompute_pad(keypad)
        directional_pad_transitions = cls.precompute_pad(directional_pad)

        # we have something like:
        #     historian hall   |   -40 degree cols zone  |     irradiated zone     | depressurized zone
        # me --> direction pad | robot --> direction pad | robot --> direction pad | robot --> keypad
        #
        # This means we have num_robots -1 robots that are using keypads.
        #

        result = 0
        for key_code in file_content:
            keypad_entry_sequences = cls.get_keypad_entry_sequences(content.ACTIVATE + key_code, keypad_transitions)

            shortest_sequence = -1
            for keypad_entry_sequence in keypad_entry_sequences:
                sequence = "".join(keypad_entry_sequence)

                number_of_presses = cls.compute_length(sequence, number_of_robots, directional_pad_transitions)
                if -1 == shortest_sequence or number_of_presses < shortest_sequence:
                    shortest_sequence = number_of_presses
            result = result + (shortest_sequence * int(key_code.replace(content.ACTIVATE, "")))
        return result

    @classmethod
    def get_keypad_entry_sequences(
        cls, key_code: str, keypad_transitions: dict[str, dict[str, list[str]]]
    ) -> list[tuple[str, ...]]:
        code_list = list(key_code)
        combos = []
        for index in range(1, len(code_list)):
            start = code_list[index - 1]
            end = code_list[index]

            transitions = keypad_transitions[start][end]
            combos.append(transitions)

        result = list(itertools.product(*combos))

        return result

    @classmethod
    def compute_length(cls, sequence, depth, keypad_transitions: dict[str, dict[str, list[str]]]):
        if depth == 1:
            full_sequence = content.ACTIVATE + sequence  # Always moving from the A key
            length = 0
            for index in range(1, len(full_sequence)):
                start = full_sequence[index - 1]
                end = full_sequence[index]
                length = length + len(keypad_transitions[start][end][0])  # All the same length so take the first
            return length

        length = 0
        full_sequence = content.ACTIVATE + sequence  # Always moving from the A key
        for index in range(1, len(full_sequence)):
            start = full_sequence[index - 1]
            end = full_sequence[index]
            min_length = -1
            for next_sequence in keypad_transitions[start][end]:
                next_sequence_length = cls.compute_length(next_sequence, depth - 1, keypad_transitions)
                if -1 == min_length or next_sequence_length < min_length:
                    min_length = next_sequence_length
            length = length + min_length
        return length

    #
    #
    # BELOW HERE ALL CODE IS RELATED TO KEYPAD TRANSITION SEQUENCE GENERATION
    #
    #
    @classmethod
    def precompute_pad(cls, grid: list[list[str]]) -> dict[str, dict[str, list[str]]]:
        # Build a dict of dicts so we can go from start to end and get shorted route.
        # {
        # A: {0: ["<A"]}
        # 0: {2: ["^A"]}
        # 2: {9: [">^^A", "^>^A", "^^>A"]}
        # 9: {A: ["vvvA"]}
        # }

        key_coords = cls.get_key_coords(grid)
        key_pairs = cls.get_key_pairs(list(key_coords.keys()))
        transitions: dict[str, dict[str, list[str]]] = {}
        for start_key, end_key in key_pairs:
            if start_key == end_key:
                key_transitions = transitions.get(start_key, {})
                key_transitions[end_key] = [content.ACTIVATE]
                transitions[start_key] = key_transitions
                continue

            shortest_paths = cls.get_shortest_transitions(start_key, end_key, key_coords, grid)
            key_transitions = transitions.get(start_key, {})
            key_transitions[end_key] = shortest_paths
            transitions[start_key] = key_transitions

        return transitions

    @classmethod
    def get_shortest_transitions(
        cls, start_key: str, end_key: str, key_coords: dict[str, Point], grid: list[list[str]]
    ) -> list[str]:
        shortest_transitions = []

        lowest_cost = float("inf")
        step_queue: deque[tuple[Point, str]] = deque()
        step_queue.append((key_coords[start_key], ""))
        while len(step_queue) > 0:
            point, path = step_queue.popleft()

            moves = cls.get_available_moves(point, grid)

            not_optimal = False
            for next_point, direction in moves:
                if key_coords[end_key] == next_point:
                    if len(path) > lowest_cost:
                        not_optimal = True
                        break
                    lowest_cost = len(path)
                    shortest_transitions.append(path + direction + content.ACTIVATE)
                else:
                    step_queue.append((next_point, path + direction))
            if not_optimal:
                break
        return shortest_transitions

    @classmethod
    def get_key_coords(cls, grid: list[list[str]]) -> dict[str, Point]:
        coords = {}
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if len(grid[row][col]) > 0:
                    coords[grid[row][col]] = Point(col, row)
        return coords

    @classmethod
    def get_key_pairs(cls, keys: list[str]) -> list[tuple[str, str]]:
        pairs = []
        for start_key in keys:
            for end_key in keys:
                pairs.append((start_key, end_key))
        return pairs

    @classmethod
    def get_available_moves(cls, start_point: Point, map: list[list[str]]) -> list[tuple[Point, str]]:
        available_moves = []
        if start_point.x - 1 >= 0 and len(map[start_point.y][start_point.x - 1]) > 0:
            # can move left
            left_point = Point(start_point.x - 1, start_point.y)
            available_moves.append((left_point, move.LEFT))
        if start_point.y - 1 >= 0 and len(map[start_point.y - 1][start_point.x]) > 0:
            # can move up
            up_point = Point(start_point.x, start_point.y - 1)
            available_moves.append((up_point, move.UP))
        if start_point.x + 1 < len(map[start_point.y]) and len(map[start_point.y][start_point.x + 1]) > 0:
            # can move right
            right_point = Point(start_point.x + 1, start_point.y)
            available_moves.append((right_point, move.RIGHT))
        if start_point.y + 1 < len(map) and len(map[start_point.y + 1][start_point.x]) > 0:
            # can move down
            down_point = Point(start_point.x, start_point.y + 1)
            available_moves.append((down_point, move.DOWN))

        return available_moves
