from project.mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Vancho","Elephant","Mooo")

    def test_successful_init(self):
        self.assertEqual("Vancho", self.mammal.name)
        self.assertEqual("Elephant", self.mammal.type)
        self.assertEqual("Mooo", self.mammal.sound)
        self.assertEqual("animals",self.mammal._Mammal__kingdom)

    def test_successful_make_sound_str(self):
        result = self.mammal.make_sound()
        self.assertEqual("Vancho makes Mooo", result)

    def test_successful_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_successful_get_info(self):
        result = self.mammal.info()
        self.assertEqual("Vancho is of type Elephant",result )


if __name__ == '__main__':
    main()
