import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    filename_input, filename_output = sys.argv[1:3]
    check_extension(filename_input)
    content = open_file(filename_input)
    convert_file(content, filename_output)


def convert_file(content, filename_output):
    with open(filename_output, "w") as File:
        field_names = ["first", "last", "house"]
        writer = csv.DictWriter(File, fieldnames=field_names)
        writer.writeheader()
        for row in content:
            writer.writerow(row)


def open_file(filename):
    content = []
    try:
        with open(filename) as File:
            header = csv.DictReader(File)
            for row in header:
                last, first = row["name"].split(",")
                content.append(
                    {"last": last, "first": first.lstrip(), "house": row["house"]}
                )
    except FileNotFoundError:
        sys.exit("File does not exist")
    else:
        return content


def check_extension(filename_input):
    try:
        ext = filename_input.split(".")[1]
        if not ext == "csv":
            sys.exit("Not a CSV file")
        return filename_input
    except:
        sys.exit("Not a CSV file")


main()
