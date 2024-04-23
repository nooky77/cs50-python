import sys
import inflect

def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            name = input("Name: ").strip()
            names.append(name)
        except(EOFError):
            print()
            print("Adieu, adieu, to", p.join(names))
            break

main()