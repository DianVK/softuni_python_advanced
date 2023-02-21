from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("bkkinza", 1, 20, 10)

    def test_successful_init(self):
        self.assertEqual("bkkinza", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(20, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_enemy_and_hero_with_same_username_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            data = Hero("bkkinza", 99, 99.9, 50.5)
            self.hero.battle(data)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_with_zero_or_negative_health_raise_value_error(self):
        enemy_hero = Hero("bksascho", 199, 199.9, 150.5)
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_with_zero_or_negative_health_raise_value_error(self):
        enemy_hero = Hero("bksascho", 199, 0, 150.5)
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(enemy_hero)
        self.assertEqual("You cannot fight bksascho. He needs to rest", str(ve.exception))

    def test_battle_success_battle_draw(self):
        self.hero.damage = 20
        enemy_hero = Hero("bksascho", 1, 20, 20)
        result = self.hero.battle(enemy_hero)

        self.assertEqual("Draw", result)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, enemy_hero.health)

    def test_battle_success_battle_win(self):
        enemy_hero = Hero("bksascho", 1, 20, 2)
        self.hero.damage = 20
        result = self.hero.battle(enemy_hero)
        self.assertEqual("You win", result)
        self.assertEqual(23, self.hero.health)
        self.assertEqual(0, enemy_hero.health)

    def test_successful_battle_hero_lose(self):
        enemy_hero = Hero("bksascho", 1, 20, 25)
        result = self.hero.battle(enemy_hero)
        self.assertEqual("You lose", result)
        self.assertEqual(-5, self.hero.health)
        self.assertEqual(15, enemy_hero.health)

    def test__str__(self):
        result = self.hero.__str__()
        self.assertEqual("Hero bkkinza: 1 lvl\n" 
               "Health: 20\n" 
               "Damage: 10\n", result)

if __name__ == '__main__':
    main()
