# Standard Library
import unittest

# From apps
from day_01.task_02 import Task02
from tests.test_utils.get_input import get_input


class TestTask02(unittest.TestCase):
    def test_failure(self):
        file_content = ["1234"]

        self.assertRaises(ValueError, Task02.solve, file_content)

    def test_example_input_01(self):
        file_content = get_input("tests/day_01/input_example_01.txt")

        expected = 31

        result = Task02.solve(file_content)
        assert result == expected

    def xtest_real_input(self):
        file_content = get_input("tests/day_01/input.txt")

        expected = 18650129

        result = Task02.solve(file_content)
        assert result == expected
