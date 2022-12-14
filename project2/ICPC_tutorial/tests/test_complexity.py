import pytest
import import_path
from main import (
    complexity
)

test_cases: list = [
    (1, 1, 1), #factorial cases
    (1, 2, 2),
    (1, 3, 6),
    (1, 4, 24),
    (1, 5, 120),
    (2, 1, 2), #exponential cases
    (2, 2, 4),
    (2, 3, 8),
    (2, 4, 16),
    (3, 1, 1), #quartic cases
    (3, 2, 16),
    (3, 3, 81),
    (3, 4, 256),
    (4, 1, 1), #cubic cases
    (4, 2, 8),
    (4, 3, 27),
    (5, 1, 1), #quadratic cases
    (5, 2, 4),
    (5, 3, 9),
    (6, 1, 0), #logarithmic cases
    (6, 2, 2),
    (7, 1, 1), #linear cases
    (7, 2, 2),
    (7, 3, 3),
    (7, 4, 4),
    (7, 5, 5),
    (7, 6, 6),
    (7, 7, 7)
]

@pytest.mark.parametrize('test', list(range(len(test_cases))))
def test_can_finish_adventure(test: int):
    t, n, answer = test_cases[test]

    assert complexity(t, n) == answer