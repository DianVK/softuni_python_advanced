class Jockey:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name should contain at least one character!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 18:
            raise ValueError("Jockeys must be at least 18 to participate in the race!")
