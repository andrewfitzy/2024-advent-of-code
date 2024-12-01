# Standard Library
import unittest

# From apps
from day_xx.task_02 import Task02
from tests.test_utils.get_input import get_input


class TestTask02(unittest.TestCase):
    def test_example_input(self):
        file_content = get_input("tests/day_xx/input_example.txt")

        expected = 10

        result = Task02.solve(file_content)
        assert result == expected

    def xtest_real_input(self):
        file_content = get_input("tests/day_xx/input.txt")

        expected = 10

        result = Task02.solve(file_content)
        assert result == expected
