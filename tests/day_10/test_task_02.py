# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_10.task_02 import Task02
from tests.test_utils.get_input import get_input


class TestTask02(unittest.TestCase):
    def test_example_input_05(self):
        file_content = get_input("tests/day_10/input_example_05.txt")

        expected = 81

        result = Task02.solve(file_content)
        assert result == expected

    def test_example_input_06(self):
        file_content = get_input("tests/day_10/input_example_06.txt")

        expected = 3

        result = Task02.solve(file_content)
        assert result == expected

    def test_example_input_07(self):
        file_content = get_input("tests/day_10/input_example_07.txt")

        expected = 13

        result = Task02.solve(file_content)
        assert result == expected

    def test_example_input_08(self):
        file_content = get_input("tests/day_10/input_example_08.txt")

        expected = 227

        result = Task02.solve(file_content)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_10/input.txt")

        expected = 1801

        result = Task02.solve(file_content)
        assert result == expected
