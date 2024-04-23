import re
import sys


def main():
    result = convert(input("Hours: "))
    print(result)


def convert(s):
    matches = re.search(
        r"([1-9][0-2]?)\:?([0-5][0-9])?\s(AM|PM)\sto\s([1-9][0-2]?)\:?([0-5][0-9])?\s(AM|PM)",
        s,
    )
    if matches:
        hour1, minute1, time1 = (
            int(matches.group(1)),
            matches.group(2),
            matches.group(3),
        )
        hour2, minute2, time2 = (
            int(matches.group(4)),
            matches.group(5),
            matches.group(6),
        )
        newHour1 = time(hour1, minute1, time1)
        newHour2 = time(hour2, minute2, time2)
        return f"{newHour1} to {newHour2}"
    else:
        raise ValueError


def time(hour, minute, time):
    if time == "AM":
        if hour == 12:
            hour = 00
    else:
        if hour == 12:
            hour = 12
        else:
            hour += 12
    if minute == None:
        minute = 00
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
