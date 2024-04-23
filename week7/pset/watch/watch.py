import re


def main():
    url = input("HTML: ")
    print(parse(url))


def parse(s):
    matches = re.search(
        r"\<iframe\s(?:.*\=.*\s)*src=\"(https?:\/\/(www\.)?youtube\.com\/embed\/\w*)\"",
        s,
        re.IGNORECASE,
    )
    if matches:
        found = matches.group(1)
        replaced = re.sub(
            r"https?:\/\/(www\.)?youtube\.com\/embed", "https://youtu.be", found
        )
        return replaced
    else:
        return "None"


if __name__ == "__main__":
    main()
