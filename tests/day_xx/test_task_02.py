# From apps
from day_xx.task_02 import solve
from tests.test_utils.get_input import get_input


def test_example_input():
    file_content = get_input("tests/day_xx/input_example.txt")

    expected = 10

    result = solve(file_content)
    assert result == expected


def xtest_real_input():
    file_content = get_input("tests/day_xx/input.txt")

    expected = 10

    result = solve(file_content)
    assert result == expected
