# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_16.task_02 import Task02
from tests.test_utils.get_input import get_input


class TestTask02(unittest.TestCase):
    def test_example_input_01(self):
        file_content = get_input("tests/day_16/input_example_01.txt")

        expected = 45

        result = Task02.solve(file_content)
        assert result == expected

    def test_example_input_02(self):
        file_content = get_input("tests/day_16/input_example_02.txt")

        expected = 64

        result = Task02.solve(file_content)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def xtest_real_input(self):
        file_content = get_input("tests/day_16/input.txt")

        expected = 10

        result = Task02.solve(file_content)
        assert result == expected
