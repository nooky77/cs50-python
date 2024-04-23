# check nbr of args
# if < 2 exit Too few command-line arguments
# if > 2 exit Too many command-line arguments
# check if arg is a .csv

import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    filename = check_extension(sys.argv[1])
    content = open_file(filename)
    print(tabulate(content, headers="firstrow", tablefmt="grid"))


def open_file(filename):
    content = []
    try:
        with open(filename) as File:
            reader = csv.reader(File)
            for row in reader:
                content.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return content


def check_extension(filename):
    try:
        ext = filename.split(".")[1]
    except:
        sys.exit("Not a CSV file")
    else:
        if not ext == ("csv"):
            sys.exit("Not a CSV file")
        return filename


main()
