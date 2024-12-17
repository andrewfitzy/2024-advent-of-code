# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_13.task_01 import Task01
from tests.test_utils.get_input import get_input


class TestTask01(unittest.TestCase):
    def test_example_input_01(self):
        file_content = get_input("tests/day_13/input_example_01.txt")

        expected = 480

        result = Task01.solve(file_content)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_13/input.txt")

        expected = 30413

        result = Task01.solve(file_content)
        assert result == expected