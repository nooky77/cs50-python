# name = input("Name? ")

# Write to a file
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# Read a file

with open("names.txt") as file:
    for line in file:
        print("Hello", line.rstrip())