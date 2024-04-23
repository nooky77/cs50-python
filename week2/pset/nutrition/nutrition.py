fruits_list = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plumes": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80,
}

def main():
    fruit = input("Item: ").lower()
    check_calories(fruit, fruits_list)

def check_calories(fruit, fruits_list):
    if fruit in fruits_list:
        print("Calories:", fruits_list[fruit])

main()