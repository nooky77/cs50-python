name = input("Name: ").lower()

match name:
    case "harry" | "hermione" | "ron":
        print("Griffondor")
    case "david":
        print("Hufflepuff")
    case "draco":
        print("Slytherin")
    case "lexi":
        print("Ravenclaw")
    case _:
        print("Who?")