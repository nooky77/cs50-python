def main():
    while True:
        fractions = input("Fraction: ").strip()
        result = convert(fractions)
        if result:
            break
    fuel = gauge(result)
    print(fuel)

def convert(fractions):
    try:
        x, y = fractions.split("/")
        x, y = int(x), int(y)
        if y == 0:
            raise(ZeroDivisionError)
        if 0 <= x <= y:
            return (x / y) * 100
    except(ValueError):
        raise(ValueError)


def gauge(amount):
    if amount <= 1:
        return "E"
    elif amount >= 99:
        return "F"
    else:
        return str(int(amount)) + "%"


if __name__ == "__main__":
    main()
