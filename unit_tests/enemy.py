import unittest
from unittest.mock import MagicMock
from rpg.enemy import Enemy


class TestEnemy(unittest.TestCase):
    def test_attack_hits(self):
        """Test the attack method when it hits the player"""
        enemy = Enemy("Tuco", 50, 10)
        mock_player = MagicMock()
        mock_player.health = 100
        mock_player.name = "Hero"
        with unittest.mock.patch(
            "random.random", return_value=0.5
        ), unittest.mock.patch("random.randint", return_value=10):
            enemy.attack(mock_player)

        self.assertEqual(mock_player.health, 90)

    def test_attack_miss(self):
        """Test the attack method when it misses"""
        enemy = Enemy("Tuco", 50, 10)

        mock_player = MagicMock()
        mock_player.health = 100
        mock_player.name = "Walter"

        with unittest.mock.patch("random.random", return_value=0.1):
            enemy.attack(mock_player)

        self.assertEqual(mock_player.health, 100)

    def test_attack_critical_hit(self):
        """Test the attack method when it results in a critical hit"""
        enemy = Enemy("Orc", 50, 10)

        mock_player = MagicMock()
        mock_player.health = 100
        mock_player.name = "Walter"

        with unittest.mock.patch(
            "random.random", side_effect=[0.5, 0.05]
        ), unittest.mock.patch("random.randint", return_value=10):
            enemy.attack(mock_player)

        self.assertEqual(mock_player.health, 85)


if __name__ == "__main__":
    unittest.main()
