import unittest
from unittest.mock import patch
from rpg.player import Player
from rpg.room import Room
from rpg.game import Game
from rpg.enemy import Enemy
from rpg.dealer import Dealer
from io import StringIO


class TestCombatAndDealerInSameRoom(unittest.TestCase):
    @patch(
        "builtins.input",
        side_effect=[
            "0",  # Look around the room
            "2",  # Look for company (find the enemy - Spider)
            "0",  # choose enemy
            "0",  # choose to attack
            "0",  # attack again if miss
            "0",  # attack again if miss
            "0",  # attack again if miss
            "-1",  # quit the npc selection menu
            "1",  # look for way out
            "0",  # choose door to room 2
            "0",  # look around
            "2",  # look for company
            "1",  # choose the dealer
            "0",  # buy the weapon upgrade
            "-1",  # quit npc selection menu
            "-1",  # quit game
        ],
    )
    @patch("sys.stdout", new_callable=StringIO)
    def test_game_with_combat_and_room_transition(self):
        room1 = Room("Gryffindor common room")
        room2 = Room("Dealer's room")

        spider = Enemy(description="Spider", health=14, damage=10)
        dealer = Dealer(description="A shady figure")

        room1.add_npc(spider)
        room1.add_npc(dealer)

        room1.add_door("black door", room2)

        player = Player(name="Harry Potter", room=room1, health=50, damage=10)
        player.money = 30
        game = Game(player)

        game.show_menu()

        self.assertEqual(
            spider.health,
            0,
            msg=f"Expected Spider's health to be 0, but found {spider.health}",
        )

        self.assertEqual(
            player.room.description,
            "Dealer's room",
            msg=f"Expected 'Dealer's room' but found "
                f"'{player.room.description}'",
        )


if __name__ == "__main__":
    unittest.main()
