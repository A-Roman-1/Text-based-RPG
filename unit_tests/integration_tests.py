import unittest
from unittest.mock import patch
from rpg.player import Player
from rpg.room import Room
from rpg.enemy import Enemy
from rpg.dealer import Dealer


class TestPlayerEnemyInteraction(unittest.TestCase):
    def test_player_attacks_enemy(self):
        """Test the interaction between player and enemy during combat"""
        room = Room("Battle Room")
        player = Player(name="Walter White", room=room, health=100, damage=15)
        enemy = Enemy(description="Cartel Member", health=30, damage=10)

        room.add_npc(enemy)

        with patch("random.randint", return_value=15):
            player.attack(enemy)

        self.assertEqual(
            enemy.health, 15, "Expected enemy health to be 15 after attack."
        )

    def test_enemy_attacks_player(self):
        """Test the interaction between enemy and player during combat"""
        room = Room("Battle Room")
        player = Player(name="Walter White", room=room, health=100, damage=15)
        enemy = Enemy(description="Cartel Member", health=30, damage=10)

        with patch("random.randint", return_value=10):
            enemy.attack(player)

        self.assertEqual(
            player.health, 90, "Expected player health to "
                               "be 90 after enemy attack."
        )


class TestPlayerDealerInteraction(unittest.TestCase):
    def test_player_buys_weapon_upgrade(self):
        """Test the interaction between player and dealer during a trade"""
        room = Room("Dealer's Room")
        player = Player(name="Walter White", room=room, health=100, damage=15)
        dealer = Dealer(description="Skinny Pete")

        room.add_npc(dealer)

        player.money = 30

        dealer.sell_item(player, "weapon upgrade")

        self.assertEqual(
            player.damage, 18, "Expected player's damage to increase by 20%."
        )
        self.assertEqual(
            player.money,
            15,
            "Expected player to have 15 money left after buying "
            "the weapon upgrade.",
        )

    def test_player_buys_health_potion(self):
        """Test the interaction between player and dealer during a trade"""
        room = Room("Dealer's Room")
        player = Player(name="Walter White", room=room, health=50, damage=15)
        dealer = Dealer(description="Skinny Pete")

        room.add_npc(dealer)

        player.money = 30

        dealer.sell_item(player, "max HP potion")

        self.assertEqual(
            player.health,
            player._max_health,
            "Expected player's health to be fully restored.",
        )
        self.assertEqual(
            player.money,
            10,
            "Expected player to have 10 money left after "
            "buying health potion.",
        )


class TestRoomTransition(unittest.TestCase):
    def test_room_transition(self):
        """Test room transitions (moving from one room to another)"""
        room1 = Room("Living Room")
        room2 = Room("Lab")

        room1.add_door("lab door", room2)

        player = Player(name="Walter White", room=room1, health=100, damage=15)

        player.room.doors[0].interact(player)

        self.assertEqual(
            player.room.description,
            "Lab",
            "Expected player to transition to the Lab room.",
        )


if __name__ == "__main__":
    unittest.main()
