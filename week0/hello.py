name = input("Name? ").strip().title()

first, last = name.split(" ")

def printHello(string):
    return print(f"Hello, {first}")

printHello(name)