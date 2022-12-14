def get_input():
    out = input().split()
    
    for i in range(len(out)):
        out[i] = int(out[i])
    
    return tuple(out)
    
def process(data: tuple) -> str:
    items, a, b, c = data
    result = 'impossible'
    
    if(2*items >= a + b + c):
        result = 'possible'
        
    return result
    
def main():
    
    data = get_input()
    output = process(data)
    
    print(output)
    
if __name__ == '__main__':
    main()
    
    