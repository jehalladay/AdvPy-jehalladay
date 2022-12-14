'''
Warehouse Kattis Problem
'''

def get_input():
    num_test_cases: int = int(input())
    test_cases = []

    for _ in range(num_test_cases):
        items: int = int(input())
        item_list = []
        for _ in range(items):
            item_list.append(input())

        test_cases.append(item_list)

    return test_cases


def process(data):
    output = []
    for shipment in data:
        item_map = {}
        for item in shipment:
            it, num = item.split()
            num = int(num)

            if it in item_map:
                item_map[it] += num
            else:
                item_map[it] = num

        item_map = {item: count for item, count in sorted(item_map.items(), key = lambda item: (-item[1], item[0]))}

        output.append(item_map)


    return output
    

def main():
    data = get_input()
    output = process(data)

    for item_map in output:
        print(len(item_map))
        for item, count in item_map.items():
            print(item, count)

if __name__ == '__main__':
    main()