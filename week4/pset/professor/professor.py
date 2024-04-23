import random


def main():
    level = get_level()
    round = 0
    score = 0
    while round < 10:
        # generate 2 numbers
        x = generate_integer(level)
        y = generate_integer(level)
        guess = 3
        while True:
            # if no more chance, print result and break
            if guess == 0:
                print(f"{x} + {y} = {x + y}")
                round += 1
                break
            try:
                # print calculation with input
                print(f"{x} + {y} = ", end="")
                answer = int(input())
            except ValueError:
                guess -= 1
                print("EEE")
                pass
            else:
                # if anwser right, break loop
                if x + y == answer:
                    round += 1
                    score += 1
                    break
                else:
                    guess -= 1
                    print("EEE")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 0 < level < 4:
                return level


def generate_integer(level):
    if level == 1:
        start = 0
        difficulty = 9
    elif level == 2:
        start = 10
        difficulty = 99
    else:
        start = 100
        difficulty = 999
    return random.randint(start, difficulty)


if __name__ == "__main__":
    main()
