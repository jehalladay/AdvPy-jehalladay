
import pytest
import import_path

from main import (
    process
)

# item_1: str = 'stuff'
# item_2: str = 'things'
# item_3: str = 'junk'

# test_cases = [
#     [
#         [{
#             item_1: 1,
#             item_2: 2,
#             item_3: 3
#         }],

#     ]
# [{
#     item_1: 1,
#     item_2: 7,
#     item_3: 3
# }],
# [{
#     item_1: 1,
#     item_2: 7,
#     item_3: 12
# }],
# [{
#     item_1: 1,
#     item_2: 7,
#     item_3: 12
# }],
# ]


test_cases: list = [
    
]





@pytest.mark.parametrize('test', list(range(len(test_cases))))
def test_process(test: int):
    num1, num2, answer = test_cases[test]

    assert process((num1, num2)) == answer
