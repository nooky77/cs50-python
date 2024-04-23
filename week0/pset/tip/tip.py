def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # remove the leading $, and return amount as a float
    return float(d.lstrip("$"))


def percent_to_float(p):
    # remove the trailing %, and return percentage as a float
    p = float(p.rstrip("%"))
    return p / 100

main()