


def get_input() -> tuple:
    return (
        [int(x) for x in input().split()],
        [int(x) for x in input().split()],
    )


def attacked(dog, person) -> bool:
    period: int = person % (dog[0] + dog[1])

    return period <= dog[0] and period != 0
        

def attack_count(dogs, person) -> int:
    print(dogs, person)

    dog_1 = dogs[0:2]
    dog_2 = dogs[2:4]

    return int(attacked(dog_1, person)) + int(attacked(dog_2, person))

def main():
    dogs, people = get_input()

    for person in people:
        count: int = attack_count(dogs, person)


        if count == 0:
            print('none')
        elif count == 1:
            print('one')
        else:
            print('both')


if __name__ == "__main__":
    main()