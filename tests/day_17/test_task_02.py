# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_17.task_02 import Task02
from tests.test_utils.get_input import get_input


class TestTask02(unittest.TestCase):
    """
    Note to future self: input_example_01.txt can't generate itself so ends in an infinite loop.
    """

    def test_example_input_02(self):
        file_content = get_input("tests/day_17/input_example_02.txt")

        expected = 117440

        result = Task02.solve(file_content)
        assert result == expected

    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_17/input.txt")

        expected = 105734774294938

        result = Task02.solve(file_content)
        assert result == expected
