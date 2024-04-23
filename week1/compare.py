x = int(input("x: "))
y = int(input("y: "))

if x > y:
    print("x is greater than y")
elif x < y:
    print("y is greater than x")
else:
    print("x and y are equals")

if x > y or x < y:
    print("x and y are not equals")
else:
    print("x and y are equals")
