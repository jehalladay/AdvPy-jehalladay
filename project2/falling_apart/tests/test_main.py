import pytest
import import_path
from main import (
    tuple_pack,
    split_function,
    input_function
)



# def test_function():
#     assert tuple_pack('1 2 3 4 5') == (5, 4, 3, 2, 1)                       #initial test, making sure a string is converted into a tuple
#     assert tuple_pack('  1 2 5 3 4') == (5, 4, 3, 2, 1)                     #Second test, made sure abnormally ordered strings get ordered into a tuple from largest to smallest
#     assert tuple_pack(' 1 g b d 2 3 4 5 e 7') == (7, 5, 4, 3, 2, 1)         #Third test, made sure it can handle non number characters and return only intergers

#     x = (9, 7, 6, 4, 2, 1)
#     assert split_function(x) == (17, 12)                   #initial test, made sure it functions with an input tuple of n length and outputs a tuple of length 2
#     x = (11, 6, 5, 3, 2, 2, 1)
#     assert split_function(x) == (19, 11)               #second test, made sure function accepts a larger tuple but still returns a tuple of length 2
#     x = (9, 9, 9, 9, 5, 4, 2, 1, 1, 1, 1)
#     assert split_function(x) == (27, 24)    #Third test, made sure function accepts repeating digits and handles them correctly

#     x = '1 2 3 5'
#     assert input_function(4, x) == (5, 3, 2, 1)                             #Initial test, function takes a string of 4 chars and an input of 4, returns tuple
#     assert input_function(5, x) == False                                    #Second test, function takes an interger of greater number than the total number of pieces
#     assert input_function(33) == '!=1-15'                                   #Third test, makes sure the function's inputs aren't larger than 15
#     assert input_function(-33) == '!=1-15'                                  #Fourth test, makes sure the function's inputs arent smaller than 1

#     return True



test_cases_tuple: list = [
    ('1 2 3 4 5', (5, 4, 3, 2, 1)),    #initial test, making sure a string is converted into a tuple
    ('  1 2 5 3 4', (5, 4, 3, 2, 1)),   #Second test, made sure abnormally ordered strings get ordered into a tuple from largest to smallest
    (' 1 g b d 2 3 4 5 e 7', (7, 5, 4, 3, 2, 1))   #Third test, made sure it can handle non number characters and return only intergers
]

test_cases_split: list = [
    ((9, 7, 6, 4, 2, 1), (17, 12)),                   #initial test, made sure it functions with an input tuple of n length and outputs a tuple of length 2
    ((11, 6, 5, 3, 2, 2, 1), (19, 11)),               #second test, made sure function accepts a larger tuple but still returns a tuple of length 2
    ((9, 9, 9, 9, 5, 4, 2, 1, 1, 1, 1), (27, 24))     #Third test, made sure function accepts repeating digits and handles them correctly
]

test_cases_input: list = [
    (4, '1 2 3 5', (5, 3, 2, 1)),                             #Initial test, function takes a string of 4 chars and an input of 4, returns tuple
    (5, '1 2 3 5', False),                                    #Second test, function takes an interger of greater number than the total number of pieces
    (33, '', '!=1-15'),                                       #Third test, makes sure the function's inputs aren't larger than 15
    (-33, '', '!=1-15')                                       #Fourth test, makes sure the function's inputs arent smaller than 1
]

@pytest.mark.parametrize('test', list(range(len(test_cases_tuple))))
def test_tuple_pack(test: int):
    x, answer = test_cases_tuple[test]
    assert tuple_pack(x) == answer


    
@pytest.mark.parametrize('test', list(range(len(test_cases_split))))
def test_split_function(test: int):
    x, answer = test_cases_split[test]
    assert split_function(x) == answer


@pytest.mark.parametrize('test', list(range(len(test_cases_input))))
def test_input_function(test: int):
    x, y, answer = test_cases_input[test]
    assert input_function(x, y) == answer
