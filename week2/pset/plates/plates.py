def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):
    # variable to count number
    isNumber = 0
    # len must be > 1 and < 7
    if len(str) < 2 or len(str) > 6:
        return False
    for i in range(len(str)):
        # check if char if alphanumeric
        if not str[i].isalnum():
            return False
        # check if 1st 2 char are letter and uppercase
        if i < 2:
            if not str[i].isupper():
                return False
        # check if char is numb and char that follow is too
        if i > 1:
            # check if char if a numb, if it's 0, and 1st number appearing
            if str[i].isdigit():
                # if its a number increase numb variable
                isNumber += 1
                if str[i] == "0" and isNumber == 1:
                    return False
            # check if there is a char after i
            if i < len(str) - 1:
                if str[i].isdigit() and not str[i + 1].isdigit():
                    return False
    return True

main()