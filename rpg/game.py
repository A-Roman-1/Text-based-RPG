from .io_utils import Scanner
from .io_utils import Saver
from .player import Player
from .room import Room
from .door import Door
from .enemy import Enemy
from .dealer import Dealer
from JsonSerializable import JsonSerializable
from typing import Any, Dict


class Game(JsonSerializable):
    def __init__(self, player):
        """Initialize the game with a player and scanner."""
        self.player = player
        self.scanner = Scanner()

    def show_menu(self) -> None:
        """Display the main game menu and process player's input."""
        while True:
            inp: str = input(
                "What do you want to do? (-1 to quit)\n(0) "
                "Look around\n(1) Look for a way out\n(2) "
                "Look for company\n(3) Quick save\n(4) Quick load\n"
            )
            try:
                action: int = self.scanner.read_int(inp, 5)
                if action == 0:
                    self.player.inspect_current_room()
                elif action == 1:
                    self.look_for_exit()
                elif action == 2:
                    self.look_for_company()
                elif action == 3:
                    self.quick_save()
                elif action == 4:
                    self.quick_load()
                elif action == -1:
                    print("Exiting menu.")
                    break
            except Scanner.InputError as e:
                print(f"Error: {e}")
                print("Please input a valid option.\n")

    def look_for_exit(self) -> None:
        """Display doors and handle the player's choice of exiting the room."""
        print("You see the following doors:")
        for index, door in enumerate(self.player.room.doors):
            print(f"({index}) {door.description}")
        while True:
            try:
                choice: int = self.scanner.read_int(
                    input("Choose a door (-1 to quit):\n"),
                    len(self.player.room.doors)
                )
                if choice != -1:
                    self.player.room.doors[choice].interact(self.player)
                    self.player.inspect_current_room()
                break
            except Scanner.InputError as e:
                print(f"Error: {e}")
                print("Please input a valid door number.\n")

    def look_for_company(self) -> None:
        """Find NPCs in the room and handle interactions."""
        if self.player.room.NPCs:
            print("You look around for someone.")
            while True:
                try:
                    for index, npc in enumerate(self.player.room.NPCs):
                        print(f"({index}) {npc.description}")
                    choice: int = self.scanner.read_int(
                        input("Choose an NPC to interact with "
                              "(-1 to quit): \n"),
                        len(self.player.room.NPCs),
                    )
                    if choice != -1:
                        selected_npc = self.player.room.NPCs[choice]
                        selected_npc.interact(self.player)
                        if isinstance(selected_npc, Enemy):
                            self.combat(selected_npc)
                        elif isinstance(selected_npc, Dealer):
                            self.trade(selected_npc)
                    else:
                        break
                except Scanner.InputError as e:
                    print(f"Error: {e}")
                    print("Please input a valid NPC number.\n")
        else:
            print("There's no one here.")

    def trade(self, dealer) -> None:
        """Handle trade interactions between the player and a dealer."""
        print(f"You have ${self.player.money}")
        print(f"The {dealer.description} is selling: ")
        while True:
            try:
                for index, (item, price) in enumerate(
                        dealer._inventory.items()):
                    print(f"({index}) {item}: ${price}")
                choice: int = self.scanner.read_int(
                    input(
                        "Which item would you like to buy? Type the number. "
                        "(-1 to quit)\n"
                    ),
                    len(dealer._inventory.keys()),
                )
                if choice != -1:
                    item = None
                    for index, key in enumerate(dealer._inventory):
                        if index == choice:
                            item = key
                    dealer.sell_item(self.player, item)
                break
            except Scanner.InputError as e:
                print(f"Error: {e}")
                print("Please input a valid item number.\n")

    def combat(self, enemy) -> None:
        """Handle combat between the player and an enemy."""
        while self.player.is_alive() and enemy.health > 0:
            try:
                action: int = self.scanner.read_int(
                    input("What do you want to do?\n(0) Attack\n"
                          "(1) Run away\n"), 2
                )
                if action == 0:
                    self.player.attack(enemy)
                    if enemy.health <= 0:
                        print(f"You defeated {enemy.description}!")
                        self.player.room.NPCs.remove(enemy)
                        self.player.money += 10
                        break
                    enemy.attack(self.player)
                    if not self.player.is_alive():
                        print("You have been defeated. Game over!")
                        exit(0)
                    print(
                        f"Your health: {self.player.health}, "
                        f"{enemy.description}'s "
                        f"health: {enemy.health}"
                    )
                elif action == 1:
                    print("You ran away!")
                    break
            except Scanner.InputError as e:
                print(f"Error: {e}")
                print("Please input a valid action.\n")

    def quick_save(self) -> None:
        """Save the current game state."""
        game_data: Dict[str, Any] = {
            "player": self.player.toJSON(),
            "room": self.player.room.toJSON(),
            "doors": [door.toJSON() for door in self.player.room.doors]
        }
        Saver.quick_save(game_data)

    def quick_load(self) -> None:
        """Load a previously saved game state."""
        game_data: Dict[str, Any] = Saver.quick_load()
        if game_data:
            self.player = Player.fromJSON(game_data["player"])
            self.player.room = Room.fromJSON(game_data["room"])
            doors_data = game_data.get("doors", [])
            self.player.room.doors = [Door.fromJSON(door_data)
                                      for door_data in doors_data]

            print("Game loaded successfully.")

    def toJSON(self) -> Dict[str, Any]:
        """Serialize the game state to a JSON-compatible format."""
        return {"player": self.player.toJSON()}

    @classmethod
    def fromJSON(cls, data: Dict[str, Any]):
        """Deserialize the game state from a JSON-compatible format."""
        player = Player.fromJSON(data["player"])
        return cls(player)
