from datetime import date
import re
import sys
import inflect

p = inflect.engine()


def main():
    date_birth = input("Time? ").strip()
    print(seasons(date_birth))


def seasons(str):
    date_input = valid_date(str)
    year, month, day = date_input
    date_now = date.today()
    date_birth = date(year, month, day)
    difference = ((date_now - date_birth).days) * 1440
    return (p.number_to_words(difference, andword="") + " minutes").capitalize()


# Checking if date is valid, returning tuple containing (YY-MM-DD)
def valid_date(date):
    result = re.match(r"^(\d{4})-(\d{2})-(\d{2})", date)
    if not result:
        sys.exit("Invalid date")
    return int(result[1]), int(result[2]), int(result[3])


if __name__ == "__main__":
    main()

# 1963-11-22
