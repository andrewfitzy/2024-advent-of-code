# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_14.task_02 import Task02
from tests.test_utils.get_input import get_input


class TestTask02(unittest.TestCase):
    def test_example_input_01(self):
        file_content = get_input("tests/day_14/input_example_01.txt")

        expected = 1

        result = Task02.solve(width=11, height=7, file_content=file_content)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_14/input.txt")

        expected = 6870

        result = Task02.solve(width=101, height=103, file_content=file_content)
        assert result == expected