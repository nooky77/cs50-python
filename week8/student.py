class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    #Getter
    @property
    def name(self):
        return self._name
    @property
    def house(self):
        return self._house

    #Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @house.setter
    def house(self, house):
        if not house in ["Red", "Blue", "Yellow"]:
            raise ValueError("Wrong house")
        self._house = house

    #Methods s
    def card(self):
        print(f"{self.name} is form house {self.house}")

def main():
    name = input("Name? ").strip()
    house = input("House? ").strip()
    student = Student(name, house)
    student.card()

main()