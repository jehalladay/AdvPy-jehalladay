def get_input():
    out = input().split()
    
    for i in range(len(out)):
        out[i] = int(out[i])
    
    return tuple(out)
    
def process(data):
    a, b = data

    return abs(a - b)
    
def main():

    while True:
        try:
            data = get_input()
            output = process(data)
            print(output)
        except:
            break


main()
    
# if __name__ == '__main__':
#     main()
    