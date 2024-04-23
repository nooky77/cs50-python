def main():
    string = input("What's your name?: ")
    print(twitter(string))

def twitter(str):
    newStr = ""
    # set list containing vowels
    vowels = ["a", "e", "i", "o", "u"]
    # loop through each char in string
    for letter in str:
        # loop through each vowels
        for vowel in vowels:
            # check if letter is a vowel
            if letter.lower() == vowel:
                break
            # if vowel is "u" aka end of list, add char to newStr
            if vowel == "u":
                newStr += letter
    return newStr
main()
