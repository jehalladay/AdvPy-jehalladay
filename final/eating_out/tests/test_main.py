
import pytest
import import_path

from main import (
    process
)

test_cases = [
    (1, 2, 3, 4, 'impossible'),
    (2, 2, 3, 4, 'impossible'),
    (1, 1, 1, 0, 'possible'),
    (1, 1, 1, 1, 'impossible'),
    (100, 1, 1, 1, 'possible'),
    (100, 1, 1, 2, 'possible'),
    (100, 100, 1, 1, 'possible')
]



@pytest.mark.parametrize('test', list(range(len(test_cases))))
def test_process(test: int):
    items, a, b, c, answer = test_cases[test]

    assert process((items, a, b, c)) == answer
