# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_14.task_01 import Task01
from tests.test_utils.get_input import get_input


class TestTask01(unittest.TestCase):
    def test_example_input_01(self):
        file_content = get_input("tests/day_14/input_example_01.txt")

        expected = 12

        result = Task01.solve(width=11, height=7, file_content=file_content)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_14/input.txt")

        expected = 218295000

        result = Task01.solve(width=101, height=103, file_content=file_content)
        assert result == expected
