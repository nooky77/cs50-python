def main():
# prompt user for fraction
    prompt = "Fraction: "
    valid_fraction = valid_numbers(prompt)
    check_fuel(valid_fraction)


# make function check is_valid
def valid_numbers(prompt):
    # make a loop to ask a valid input
    while True:
        fractions = input(prompt).strip()
        # catch error coming from input
        try:
            # split string in 2
            x, y = fractions.split("/")
            # check if x and y are int
            if x.isdigit() and y.isdigit():
                #if true then convert x and y to int
                x, y = int(x), int(y)
                # check that x <= y and y < 0
                if 0 <= x <= y:
                    # if true return x and y
                    return [x, y]
        # if not valid > catch it
        except(ValueError, ZeroDivisionError):
            print("Not a fraction, try again.")

# make fuel function, pass result from is_valid as param
def check_fuel(arr):
    x, y = arr[0], arr[1]
    # check result of fraction
    if (x / y) * 100 <= 1:
        return print("E")
    elif (x / y) * 100 >= 99:
        return print("F")
    else:
        number = int(round((x / y) * 100))
        return print(number, "%", sep="")
main()