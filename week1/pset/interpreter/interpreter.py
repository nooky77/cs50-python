def calc(x, y, z):
    match y:
        case "+":
            print(float(x + z))
    match y:
        case "-":
            print(float(x - z))
    match y:
        case "*":
            print(float(x * z))
    match y:
        case "/":
            if z == 0:
                print("Cant divide by 0")
            else:
                print(float(x / z))

def main():
    str = input("Expression: ")
    x, y, z = str.split(" ")
    x = int(x)
    z = int(z)
    calc(x, y, z)

main()