def main():
    date = date_validation(months)
    year, month, day = date
    print(f"{year:02}-{month:02}-{day:02}")


# make func is_valid to check if date input is valid
def date_validation(months_list):
    # make a loop
    while True:
        # try / except the input
        try:
            # ask the user for date
            date = input("Date: ").strip()
            # case 1: check for number of "/" == 2
            if date.count("/") == 2:
                # make 3 variable for DD MM YY and split input with "/"
                month, day, year = date.split("/")
                # convert from str to int
                month, day, year = int(month), int(day), int(year)
                # check if DD MM YY are valid numbers
                if 0 < day < 32 and 0 < month < 13 and year >= 0:
                    # return input as list [YY, MM, DD]
                    return [year, month, day]
            # case 2: check for number of "," == 1
            elif date.count(",") == 1:
                # make 2 variable for tempdate and year then split with ","
                tempdate, year = date.split(",")
                # make 2 variable for MM and DD from tempdate, split on " "
                month, day = tempdate.split(" ")
                # check if MM is in month list with count method
                if months_list.count(month) > 0:
                    # get index of month from list
                    month = months_list.index(month) + 1
                    # convert from str to int
                    day, year = int(day), int(year)
                    # check if DD and YY are valid
                    if 0 < day < 32 and year >= 0:
                        # return input as list [YY, MM, DD]
                        return [year, month, day]
        except (EOFError, ValueError):
            pass


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

main()
