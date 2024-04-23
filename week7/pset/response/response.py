from validator_collection import validators


def main():
    email = input("What's your email address? ")
    print(is_valid(email))


def is_valid(mail):
    try:
        validators.email(mail)
        return "Valid"
    except:
        return "Invalid"


main()
