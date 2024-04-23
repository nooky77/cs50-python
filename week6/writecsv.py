import csv

name = input("Name?: ").strip()
city = input("City?: ").strip()

with open("heros.csv", "a") as file:
    # Write as csv with order as fieldnames
    writer = csv.DictWriter(file, fieldnames=['name', 'city'])
    writer.writerow({"name": name, "city": city})
