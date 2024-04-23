import random
import sys

def main():
    guess()

def guess():
    while True:
        try:
            target = int(input("Level: "))
            if target < 1:
                continue
            break
        except:
            pass
    lucky_nbr = random.randint(1, target)
    guess = 0
    while True:
        try:
            guess = int(input("Guess: "))
        except:
            pass
        else:
            if guess > lucky_nbr:
                print("Too large!")
            elif guess < lucky_nbr:
                print("Too small!")
            else:
                print("Just right!")
                sys.exit()
main()