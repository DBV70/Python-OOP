from project.hero import Hero
from unittest import TestCase, main

class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero('Pesho', 5, 6.5, 3.5)
        self.enemy = Hero('Gosho', 5, 6.5, 3.5)


    def test_init(self):
        self.assertEqual('Pesho', self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(6.5, self.hero.health)
        self.assertEqual(3.5, self.hero.damage)

    def test_battle_enemy_equal_username(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_health_less_or_equal_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_less_or_equal_zero(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

        self.enemy.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        self.hero.health = 17.5
        self.enemy.health = 17.5
        self.assertEqual("Draw", self.hero.battle(self.enemy))

    def test_battle_hero_wins(self):
        self.hero.health = 100
        self.enemy.health = 17.5
        result = self.hero.battle(self.enemy)
        self.assertEqual(6, self.hero.level)
        self.assertEqual(100 - 17.5 + 5, self.hero.health)
        self.assertEqual(3.5 + 5, self.hero.damage)
        self.assertEqual("You win", result)

    def test_battle_hero_lose(self):
        self.hero.health = 17.5
        self.enemy.health = 100
        result = self.hero.battle(self.enemy)
        self.assertEqual(6, self.enemy.level)
        self.assertEqual(100 - 17.5 + 5, self.enemy.health)
        self.assertEqual(3.5 + 5, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_str(self):
        expected_result =   f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                            f"Health: {self.hero.health}\n" \
                            f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected_result, str(self.hero))

if __name__ == '__main__':
    main()
