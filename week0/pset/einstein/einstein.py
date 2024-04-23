# create func massToJoules, takes 1 input
def massToJoules(nbr):
    # output the conversion to joules as int
    joules = nbr * 300000000 ** 2
    return joules

def main():
    # prompt user for mass as int in KG
    mass = int(input("m: "))
    print(massToJoules(mass))

# call main func
main()