# Standard Library
import os
import unittest

# Dependencies
import pytest

# From apps
from day_24.task_02 import Task02
from tests.test_utils.get_input import get_input


class TestTask02(unittest.TestCase):
    @pytest.mark.skipif(
        os.environ["TEST_ENV"] == "staging", reason="My input file is not added to git, only run this locally"
    )
    def test_real_input(self):
        file_content = get_input("tests/day_24/input.txt")

        expected = "gst,khg,nhn,tvb,vdc,z12,z21,z33"

        result = Task02.solve(file_content)
        assert result == expected
