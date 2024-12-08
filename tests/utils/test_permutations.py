# Standard Library
import unittest

# From apps
from utils.permutations import get_permutations


class TestPermutations(unittest.TestCase):
    def test_get_permutations(self):
        input = ["a", "b", "c"]

        output = get_permutations(input)

        assert len(output) == 6
        assert output.count(["a", "b", "c"]) == 1
        assert output.count(["a", "c", "b"]) == 1
        assert output.count(["b", "a", "c"]) == 1
        assert output.count(["b", "c", "a"]) == 1
        assert output.count(["c", "a", "b"]) == 1
        assert output.count(["c", "b", "a"]) == 1
