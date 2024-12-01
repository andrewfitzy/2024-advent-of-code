# Standard Library
import unittest

# From apps
from day_xx.task_01 import Task01
from tests.test_utils.get_input import get_input


class TestTask01(unittest.TestCase):
    def test_example_input(self):
        file_content = get_input("tests/day_xx/input_example.txt")

        expected = 1

        result = Task01.solve(file_content)
        assert result == expected

    def xtest_real_input(self):
        file_content = get_input("tests/day_xx/input.txt")

        expected = 1

        result = Task01.solve(file_content)
        assert result == expected
