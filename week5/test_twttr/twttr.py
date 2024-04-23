def main():
    str = input("Input: ")
    print(shorten(str))


def shorten(word):
    new_str = ""
    vowels = ["a", "e", "i", "o", "u"]
    for char in word:
        for vowel in vowels:
            tmp_char = char.lower()
            if tmp_char == vowel:
                new_str += ""
                break
            if vowel == "u":
                new_str += char
    return new_str


if __name__ == "__main__":
    main()
