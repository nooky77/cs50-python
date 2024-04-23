def main():
    groceries_list = make_groceries()
    sorted_groceries(groceries_list)

# make sorted_groceries, takes dict as input
def sorted_groceries(groceries):
    # make empty list
    list = []
    # loop through dict
    for item in groceries:
        # append key into list
        list.append(item)
    # sort list
    list.sort()
    # make loop through sorted list
    for item in list:
    # print list with quantity
        print(groceries[item], item)

# make groceries func
def make_groceries():
    # create dict for storing items
    groceries_list = {}
    # make a loop for asking user items to add to dict
    while True:
        # make a try/except
        try:
            # ask user for item, trim white space and uppercase it
            item = input().strip().upper()
            # check if item is in dict
            if item in groceries_list:
                # if true, add +1 to it
                groceries_list[item] += 1
            else:
                # if false, set to 1
                groceries_list[item] = 1
        # except(EOFError)
        except(EOFError):
            # return dict
            return groceries_list

main()