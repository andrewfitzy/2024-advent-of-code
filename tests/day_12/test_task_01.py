# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_12.task_01 import Task01
from tests.test_utils.get_input import get_input


class TestTask01(unittest.TestCase):
    def test_example_input_01(self):
        file_content = get_input("tests/day_12/input_example_01.txt")

        expected = 140

        result = Task01.solve(file_content)
        assert result == expected

    def test_example_input_02(self):
        file_content = get_input("tests/day_12/input_example_02.txt")

        expected = 772

        result = Task01.solve(file_content)
        assert result == expected

    def test_example_input_03(self):
        file_content = get_input("tests/day_12/input_example_03.txt")

        expected = 1930

        result = Task01.solve(file_content)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_12/input.txt")

        expected = 1450422

        result = Task01.solve(file_content)
        assert result == expected
