def main():
    str = input("camelCase: ")
    camelStr = camel_to_snake_case(str)
    print("snake_case:", camelStr)


def camel_to_snake_case(string):
    newStr = ""
    for letter in string:
        if letter.isupper():
            newStr += "_" + letter.lower()
        else:
            newStr += letter
    return newStr

main()