# Standard Library
import re

# From apps
from utils.point import Point


class MachineConfiguration:
    button_a: Point
    button_b: Point
    prize_location: Point

    def __init__(self, button_a: Point, button_b: Point, prize_location: Point):
        self.button_a = button_a
        self.button_b = button_b
        self.prize_location = prize_location

    def __str__(self):
        return "(A={button_a}, B={button_b}, PRIZE={prize_location})".format(
            button_a=self.button_a, button_b=self.button_b, prize_location=self.prize_location
        )


class Task01:
    BUTTON_PATTERN = re.compile("Button [A|B]: X[+](\\d+), Y[+](\\d+)")
    PRIZE_PATTERN = re.compile("Prize: X=(\\d+), Y=(\\d+)")

    @classmethod
    def solve(cls, file_content: list[str]) -> int:
        machines: list[MachineConfiguration] = cls.get_machine_configs(file_content)

        result = 0
        for machine_config in machines:
            result = result + cls.calculate_optimal_presses(machine_config)

        return result

    @classmethod
    def get_machine_configs(cls, input: list[str]) -> list[MachineConfiguration]:
        machines: list[MachineConfiguration] = []
        count = 3
        while count <= len(input):
            button_a_matcher = cls.BUTTON_PATTERN.match(input[count - 3])
            assert button_a_matcher is not None  # MyPy Hack :(
            button_a = Point(x=int(button_a_matcher.group(1)), y=int(button_a_matcher.group(2)))

            button_b_matcher = cls.BUTTON_PATTERN.match(input[count - 2])
            assert button_b_matcher is not None  # MyPy Hack :(
            button_b = Point(x=int(button_b_matcher.group(1)), y=int(button_b_matcher.group(2)))

            prize_location_matcher = cls.PRIZE_PATTERN.match(input[count - 1])
            assert prize_location_matcher is not None  # MyPy Hack :(
            prize_location = Point(x=int(prize_location_matcher.group(1)), y=int(prize_location_matcher.group(2)))

            machine_config = MachineConfiguration(button_a=button_a, button_b=button_b, prize_location=prize_location)
            machines.append(machine_config)

            count = count + 4
        return machines

    @classmethod
    def calculate_optimal_presses(cls, config: MachineConfiguration) -> int:
        cost = 0
        for a_presses in range(101):
            for b_presses in range(101):
                x_location = config.button_a.x * a_presses + config.button_b.x * b_presses
                y_location = config.button_a.y * a_presses + config.button_b.y * b_presses
                if config.prize_location.x == x_location and config.prize_location.y == y_location:
                    tmp_cost = a_presses * 3 + b_presses
                    if tmp_cost < cost or cost == 0:
                        cost = tmp_cost

        return cost
