import random


def main():
    level = get_level()
    generate_integer(level)


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
    score = 0
    # set difficulty
    if level == 1:
        difficulty = 10
    elif level == 2:
        difficulty = 100
    else:
        difficulty = 1000
    # set round
    round = 0
    while round < 10:
        # generate 2 numbers
        x = random.randrange(1, difficulty)
        y = random.randrange(1, difficulty)
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


if __name__ == "__main__":
    main()
