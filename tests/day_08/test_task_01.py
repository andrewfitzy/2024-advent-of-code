# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_08.task_01 import Task01
from tests.test_utils.get_input import get_input


class TestTask01(unittest.TestCase):
    def test_example_input_01(self):
        file_content = get_input("tests/day_08/input_example_01.txt")

        expected = 14

        result = Task01.solve(file_content)
        assert result == expected

    def test_example_input_02(self):
        file_content = get_input("tests/day_08/input_example_02.txt")

        expected = 2

        result = Task01.solve(file_content)
        assert result == expected

    def test_example_input_03(self):
        file_content = get_input("tests/day_08/input_example_03.txt")

        expected = 4

        result = Task01.solve(file_content)
        assert result == expected

    def test_example_input_04(self):
        file_content = get_input("tests/day_08/input_example_04.txt")

        expected = 4

        result = Task01.solve(file_content)
        assert result == expected

    def test_example_input_05(self):
        file_content = get_input("tests/day_08/input_example_05.txt")

        expected = 3

        result = Task01.solve(file_content)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_08/input.txt")

        expected = 351

        result = Task01.solve(file_content)
        assert result == expected
