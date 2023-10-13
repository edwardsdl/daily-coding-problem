import pytest
from problems.day_001 import run

test_data = [
    ([10, 15, 3, 7], 17, True),
    ([10, 15, 3, 7], 15, False),
    ([10, 15, 3, 7], 1, False),
    ([10, 15, 3, 7], 0, False),
]


@pytest.mark.parametrize("numbers,k,expected", test_data)
def test_run_with_example(numbers: list[int], k: int, expected: bool):
    actual = run(numbers, k)

    assert actual == expected
