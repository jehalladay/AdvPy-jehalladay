"""
"""
import os


def tuple_pack(text):
    numbers = []

    for i in text.split():
        try:
            numbers = numbers + [int(i)]
        except ValueError:
            continue

    if numbers != []:
        numbers.sort(reverse=True)


    return tuple(numbers)


def split_function(x):

    alice = sum(x[0::2])
    bob = sum(x[1::2])
    return alice, bob


def input_function(text1=None, text2=None):
    if text1 == None and text2 == None:
        while text1 == None:
            text1 = input('')
            if text1 == None:
                print("Input was not a number, please enter a number")
            elif text1 < 1 or text1 > 15:
                text1 = None
        text2 = input()
    elif text1 > 15:
        return '!=1-15'
    elif text1 < 1:
        return '!=1-15'

    if text2 != None:
        text2 = tuple_pack(text2)

    if text1 != len(text2):
        return False
    else:
        return text2



def main():
    i = input_function()

    if i == False:
        print('i==False ', i)
        return
    else:
        alice, bob = split_function(i)
        print("%s %s " % (alice, bob))


if __name__ == "__main__":
    main()
