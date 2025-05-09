import unittest
from unittest.mock import MagicMock
from rpg.dealer import Dealer


class TestDealer(unittest.TestCase):
    def test_sell_item_success(self):
        """Test the sell_item method when the player has enough money"""
        dealer = Dealer("Shady Dealer")
        mock_player = MagicMock()
        mock_player.money = 20
        mock_player.damage = 10
        mock_player.health = 50
        mock_player._max_health = 50

        dealer.sell_item(mock_player, "weapon upgrade")
        self.assertEqual(mock_player.money, 5)
        self.assertAlmostEqual(mock_player.damage, 12)

        mock_player.money = 20
        mock_player.health = 10
        dealer.sell_item(mock_player, "max HP potion")
        self.assertEqual(mock_player.money, 0)
        self.assertEqual(mock_player.health, 50)

    def test_sell_item_failure(self):
        """Test the sell_item method when the player doesn't
        have enough money"""
        dealer = Dealer("Shady Dealer")
        mock_player = MagicMock()
        mock_player.money = 10

        dealer.sell_item(mock_player, "weapon upgrade")
        self.assertEqual(mock_player.money, 10)

        dealer.sell_item(mock_player, "max HP potion")
        self.assertEqual(mock_player.money, 10)


if __name__ == "__main__":
    unittest.main()
