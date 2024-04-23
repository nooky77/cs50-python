def main():
    food_order(foods)

# create fnc food_order
def food_order(foods):
    # make total variable to track total orders
    total_amount = 0
    # make a loop to ask user for food
    while True:
        # make a try/except here for catching termination of function
        try:
            # ask user for food and titlecase it
            food = input("Item: ").strip().title()
            # check if food is in the list
            if food in foods:
                # if it is, add cost to the total variable
                total_amount += foods[food]
        # catch end of function here
        except(EOFError):
            print()
            break
        else:
            # print total variable with a dollar sign before it
            print("Total: $", format(total_amount, ".2f"), sep="")


foods = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()
