# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_15.task_02 import Task02
from tests.test_utils.get_input import get_input


class TestTask02(unittest.TestCase):
    def test_example_input_01(self):
        file_content = get_input("tests/day_15/input_example_01.txt")

        expected = 1751

        result = Task02.solve(file_content)
        assert result == expected

    def test_example_input_02(self):
        file_content = get_input("tests/day_15/input_example_02.txt")

        expected = 9021

        result = Task02.solve(file_content)
        assert result == expected

    def test_example_input_03(self):
        file_content = get_input("tests/day_15/input_example_03.txt")

        expected = 618

        result = Task02.solve(file_content)
        assert result == expected

    def test_example_input_04(self):
        file_content = get_input("tests/day_15/input_example_04.txt")

        expected = 505

        result = Task02.solve(file_content)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_15/input.txt")

        expected = 1468005

        result = Task02.solve(file_content)
        assert result == expected
