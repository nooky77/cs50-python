from pyfiglet import Figlet
import sys


def main():
    f = Figlet(font="slant")
    # expect 0 or 2 args from cli
    # if not 0 or 2 > exit the program
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid usage")
    # if len is 2
    if len(sys.argv) == 3:
        #  arg1 must be -f or --font, arg2 is name of font
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        try:
            f = Figlet(font=sys.argv[2])
        except:
            sys.exit("Invalid usage")
    # ask user for str
    str = input("Input: ")
    # print str
    print("Output:")
    print(f.renderText(str))


main()
