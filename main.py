from rpg.room import Room
from rpg.player import Player
from rpg.NPC import NPC
from rpg.enemy import Enemy
from rpg.game import Game
from rpg.dealer import Dealer


def setup_rooms():
    """Creates and connects rooms for the game"""
    room1 = Room("Walter's Living Room")
    room2 = Room("Gus' Restaurant")
    room3 = Room("Meth Lab")
    room4 = Room("Car Wash")
    room5 = Room("Jesse's Basement")

    room1.add_door("front door to Gus' Restaurant", room2)
    room1.add_door("back door to Meth Lab", room3)
    room2.add_door("back door to Walter's Living Room", room1)
    room2.add_door("side door to Meth Lab", room3)
    room2.add_door("stairs to Car Wash", room4)
    room2.add_door("hidden door to Jesse's Basement", room5)
    room3.add_door("entrance to Walter's Living Room", room1)
    room3.add_door("secret passage to Gus' Restaurant", room2)
    room4.add_door("stairs down to Gus' Restaurant", room2)
    room5.add_door("trap door to Gus' Restaurant", room2)

    return room1, room2, room3, room4, room5


def add_npcs(room1, room2, room3, room4, room5):
    """Adds NPC characters to the respective rooms"""
    npc1 = NPC("Skyler White")
    npc2 = NPC("Jesse Pinkman")
    npc3 = NPC("Saul Goodman")
    npc4 = Dealer("Dealer Skinny Pete")
    npc5 = NPC("Mike Ehrmantraut")

    room1.add_npc(npc1)
    room2.add_npc(npc4)
    room3.add_npc(npc2)
    room4.add_npc(npc3)
    room5.add_npc(npc5)


def add_enemies(room2, room3, room5):
    """Adds enemies to the respective rooms."""
    cartel_member = Enemy("Cartel Member", health=30, damage=10)
    tuco = Enemy("Tuco Salamanca", health=40, damage=15)
    hector = Enemy("Hector Salamanca", health=20, damage=10)

    room3.add_npc(tuco)
    room5.add_npc(cartel_member)
    room2.add_npc(hector)


def main():
    """Initializes and runs the game by setting up rooms, NPCs, and enemies,
    and starts the game loop."""

    room1, room2, room3, room4, room5 = setup_rooms()

    player1 = Player("Walter White", room1)

    add_npcs(room1, room2, room3, room4, room5)
    add_enemies(room2, room3, room5)

    game = Game(player1)
    game.show_menu()


if __name__ == "__main__":
    main()
