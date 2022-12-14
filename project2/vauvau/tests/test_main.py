
import pytest
import import_path

from main import (
    attacked,
    attack_count
)

test_cases = [
    ((2, 2, 3, 3), (1, 3, 4), ['both', 'one', 'none']),
    ((2, 3, 4, 5), (5, 6, 7), ['none', 'one', 'one']),
    ((2, 3, 4, 5), (1, 2, 3), ['both', 'both', 'one']),
    ((2, 2, 3, 3), (5, 7, 8), ['one', 'one', 'one']),
]



@pytest.mark.parametrize('test', list(range(len(test_cases))))
def test_can_finish_adventure(test: int):
    dogs, persons, answers = test_cases[test]



    for i, person in enumerate(persons):
        answer = answers[i]
        count: int = attack_count(dogs, person)

        if count == 0:
            assert answer == 'none'
        elif count == 1:
            assert answer == 'one'
        else:
            assert answer == 'both'

