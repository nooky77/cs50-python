def main():
    prompt = input("Greeting: ").strip()
    result = value(prompt)
    print(f"${result}")


def value(greeting):
    if len(greeting) == 0:
        return 100
    elif greeting.lower() == "hello" or greeting[0:5].lower() == "hello":
        return 0
    elif greeting[0].lower() == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
