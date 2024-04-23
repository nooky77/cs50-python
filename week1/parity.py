def main():
    nbr = int(input("Number: "))
    if isEven(nbr):
        print("Even")
    else:
        print("Odd")

def isEven(n):
    # if n % 2 == 0:
    #     return True
    # else:
    #     return False
    return n % 2 == 0
main()