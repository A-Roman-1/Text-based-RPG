import unittest
from unittest.mock import MagicMock
from rpg.player import Player
from rpg.room import Room
from rpg.enemy import Enemy


class TestPlayer(unittest.TestCase):
    def setUp(self):
        """Set up a basic player and a mock room for each test"""
        self.room = Room("Test Room")
        self.player = Player(name="Hero", room=self.room, health=100,
                             damage=10)

    def test_attack_hits(self):
        """Test that the player's attack hits the enemy"""
        enemy = Enemy("Orc", 50, 10)
        with unittest.mock.patch(
            "random.random", return_value=0.5
        ), unittest.mock.patch("random.randint", return_value=10):
            self.player.attack(enemy)

        self.assertEqual(
            enemy.health,
            40,
            msg="Expected enemy health to be reduced to 40 after attack",
        )

    def test_attack_miss(self):
        """Test that the player's attack misses"""
        enemy = Enemy("Orc", 50, 10)
        with unittest.mock.patch("random.random", return_value=0.1):
            self.player.attack(enemy)

        self.assertEqual(
            enemy.health,
            50,
            msg="Expected enemy health to remain the same after a miss",
        )

    def test_attack_critical_hit(self):
        """Test that the player's attack results in a critical hit"""
        enemy = Enemy("Orc", 50, 10)
        with unittest.mock.patch(
            "random.random", side_effect=[0.5, 0.05]
        ), unittest.mock.patch("random.randint", return_value=10):
            self.player.attack(enemy)

        self.assertEqual(
            enemy.health,
            35,
            msg="Expected enemy health to be reduced to 35 after a "
                "critical hit",
        )

    def test_inspect_current_room(self):
        """Test that the player correctly inspects the current room"""
        with unittest.mock.patch("builtins.print") as mock_print:
            self.player.inspect_current_room()
            mock_print.assert_called_with("Hero sees Test Room")

    def test_health_decreases(self):
        """Test that player's health decreases correctly"""
        self.player.health = 100
        self.player.health -= 20
        self.assertEqual(
            self.player.health, 80, msg="Expected player health "
                                        "to decrease to 80"
        )

    def test_health_not_below_zero(self):
        """Test that player's health doesn't go below zero"""
        self.player.health = -10
        self.assertEqual(
            self.player.health, 0, msg="Expected player health to "
                                       "be clamped to 0"
        )

    def test_max_health_limit(self):
        """Test that player's health doesn't exceed max health"""
        self.player.health = 150
        self.assertEqual(
            self.player.health,
            100,
            msg="Expected player health to be clamped to max health (100)",
        )

    def test_money_increase(self):
        """Test that player's money increases correctly"""
        self.player.money = 10
        self.player.money += 20
        self.assertEqual(
            self.player.money, 30, msg="Expected player money to "
                                       "increase to 30"
        )

    def test_money_not_negative(self):
        """Test that setting player's money to a negative value
        raises an error"""
        with self.assertRaises(
            ValueError, msg="Expected ValueError when setting money to "
                            "a negative value"
        ):
            self.player.money = -5


if __name__ == "__main__":
    unittest.main()
