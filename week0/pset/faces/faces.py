# create func named convert, takes str
def convert(str):
    # replace all smileyface and sadfaces
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str

# create main func
def main():
    # prompt user for input
    msg = input()
    # call convert func with input from user and print
    print(convert(msg))

# call main func
main()