import math

def input_function(test=0):
    if test == 0:
        test = input()
    test = test.split()
    x = []
    for i in test:
        x += [int(i)]
    return tuple(x)

def complexity(t = 0, n = 0):
    result: int = 0

    if t == 1:
        result = math.factorial(n)
    elif t == 2:
        result = 2**n
    elif t == 3:
        result = n**4
    elif t == 4:
        result = n**3
    elif t == 5:
        result = n**2
    elif t == 6:
        result = math.log2(n)*n
    elif t == 7:
        result = n
        
    return result

def main():
    test = input_function()
    m, n, t = test
    if n > 12 and t == 1:
        print("TLE")
        return
    elif n > 29 and t == 2:
        print("TLE")
        return
    if m < complexity(t, n):
        print("TLE")
        return 'TLE'
    else:
        print('AC')

if __name__ == "__main__":
    main()
