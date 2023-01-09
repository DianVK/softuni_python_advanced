from project.animal import Animal


class Mammal(Animal):
    def __init__(self, name: str):
        self.name = name
