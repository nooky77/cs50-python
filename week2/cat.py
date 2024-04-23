# for loop
def meow1(n):
    for i in range(n):
        print("Meow!")

# while loop
def meow2(n):
    while n > 0:
        print("Meow!")
        n -= 1


def main():
    nbr = int(input("Number: "))
    meow2(nbr)

main()