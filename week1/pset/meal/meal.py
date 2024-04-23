def main():
    str = input("What time is it? ").strip()
    # convert string hour to int
    time = convert(str)
    meal(time)

def convert(str):
    # check if str contain a space
    if str.find(" ") > 0:
        # split string into hour and time of day
        time, day = str.split(" ")
        # split string into hour and minutes
        hour, minute = time.split(":")
        minute = float(minute)
        # check if am or pm
        if day == "p.m.":
            if hour == "12":
                hour = 12.0
            else:
                hour = float(hour) + 12.0
        else:
            if hour == "12":
                hour = 0.0
            hour = float(hour)
    else:
        # split string at the semicolon
        hour, minute = str.split(":")
        hour, minute = float(hour), float(minute)
    # convert hour and mintute to int
    return hour + (minute / 60)

def meal(time):
    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")

if __name__ == "__main__":
    main()