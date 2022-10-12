
def can_finish_adventure(string: str) -> str:
    items: list = []

    for c in string:
        if c == '$' or c == '*' or c == '|':
            items.append(c)
        elif c != '.':
            if len(items) > 0:
                next_item: str = items.pop()
            else:
                return "NO"
            
            if c == 'b':
                if next_item != '$':
                    return 'NO'
            elif c == 'j':
                if next_item != '*':
                    return 'NO'
            elif c == 't':
                if next_item != '|':
                    return 'NO'

    if len(items) > 0:
        return 'NO'
    return 'YES'

def main():
    
    adventures: list = []
    num_adventures: int = 0

    num_adventures = int(input())

    for _ in range(num_adventures):
        adventures.append(input())

    for adv in adventures:
        print(can_finish_adventure(adv))

if __name__ == "__main__":
    main()