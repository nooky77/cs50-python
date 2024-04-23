def main():
    number = get_number()
    printColumn(number)

def printColumn(height):
    for i in range(height):
        for _ in range(i + 1):
            print("#", end='')
        print("\n",end='')

def get_number():
    while True:
        number = int(input("Number of bricks: "))
        if number > 0:
            return number

main()