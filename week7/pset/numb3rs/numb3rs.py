import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    found = re.search(r"^(\d*)\.(\d*)\.(\d*)\.(\d*)$", ip)
    if found:
        for n in range(1, 5):
            if not 0 <= int(found.group(n)) <= 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
