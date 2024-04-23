# create function bank accept 1 arg
def bank(str):
    # if arg == "hello" output $0
    if str.startswith("hello"):
        print("$0")
    # elseif arg start with "h" but not hello output $20
    elif str.startswith("h"):
        print("$20")
    # else output $100
    else:
        print("$100")

def main():
    msg = input("Greeting: ").strip().lower()
    bank(msg)

main()