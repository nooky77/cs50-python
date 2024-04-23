# students = {
#     "Hermione": "Gryffindor",
#     "Harry": "Gryffindor",
#     "Ron": "Gryffindor",
#     "Draco": "Slytherin",
# }

# for name in students:
#     print(name, students[name], sep=", ")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus" : "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus" : "Otter"},
    {"name": "Ron", "house": "Gryffindor", "patronus" : "Otter"},
    {"name": "Draco", "house": "Slytherin", "patronus" : None},
]

for student in students:
    print(student["name"])