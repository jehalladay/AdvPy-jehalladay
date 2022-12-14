
import pytest
import import_path

from main import (
    process
)

test_cases = [
    (1, 2, 1),
    (2, 2, 0),
    (3, 2, 1),
    (4, 2, 2),
    (5, 2, 3),
    (6, 2, 4),
    (-7, -2, 5),
    (-8, -2, 6),
    (0, 9, 9),
    (0, 10, 10),
    (0, -9, 9)
]



@pytest.mark.parametrize('test', list(range(len(test_cases))))
def test_process(test: int):
    num1, num2, answer = test_cases[test]

    assert process((num1, num2)) == answer
