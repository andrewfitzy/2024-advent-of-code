# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_18.task_01 import Task01
from tests.test_utils.get_input import get_input


class TestTask01(unittest.TestCase):
    def test_example_input_01(self):
        file_content = get_input("tests/day_18/input_example_01.txt")

        expected = 22

        result = Task01.solve(file_content, 6, 12)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_18/input.txt")

        expected = 384

        result = Task01.solve(file_content, 70, 1024)
        assert result == expected