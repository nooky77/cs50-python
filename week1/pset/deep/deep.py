# create func deep
def deep(str):
    match str:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

def main():
    # prompt user
    answer = input("What is the Answer to the Great Question? ").strip().lower()
    deep(answer)

main()