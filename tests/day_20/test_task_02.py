# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_20.task_02 import Task02
from tests.test_utils.get_input import get_input


class TestTask02(unittest.TestCase):
    def test_example_input_01(self):
        file_content = get_input("tests/day_20/input_example_01.txt")

        expected = 0

        result = Task02.solve(file_content)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_20/input.txt")

        expected = 983905

        result = Task02.solve(file_content)
        assert result == expected
