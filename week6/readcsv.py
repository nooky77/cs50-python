heroes = []
# Open file. Split on a comma, and add it the a list as dict.
with open("heros.csv") as file:
    for line in file:
        hero, city = line.rstrip().split(",")
        heroes.append({"name": hero, "city": city})

# Anonymous function
# lambda x: x + x

# Print heroes list sorted by name
for hero in sorted(heroes, key=lambda heroes: heroes["city"]):
    print(f"{hero['name']} is living in {hero['city']}")