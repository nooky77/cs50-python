import sys

def main():
    list = sys.argv
    if len(list) < 2:
        sys.exit("Too few command-line arguments")
    if len(list) > 2:
        sys.exit("Too many command-line arguments")
    try:
        file_name = list[1].split(".")
        if not file_name[1] == "py":
            sys.exit("Not a Python file")
    except:
        sys.exit("Not a Python file")
    else:
        print(count_lines(sys.argv[1]))

def count_lines(filename):
    counter = 0
    try:
        with open(filename) as File:
            for row in File:
                row = row.lstrip()
                if row.startswith("#") or len(row) <= 1:
                    continue
                else:
                    counter += 1
    except:
        sys.exit("File does not exist")
    else:
        return counter

main()