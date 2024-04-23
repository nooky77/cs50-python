score = int(input("Score: "))

if 90 <= score <= 100:
    print("A")
elif 70 <= score < 90:
    print("B")
elif 50 <= score < 70:
    print("C")
else:
    print("F")