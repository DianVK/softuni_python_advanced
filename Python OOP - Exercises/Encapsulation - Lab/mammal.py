class Mammal:
    __kingdom = "animals"

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        result = f"{self.name} makes {self.sound}"
        return result

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        result = f"{self.name} is of type {self.type}"
        return result


mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
