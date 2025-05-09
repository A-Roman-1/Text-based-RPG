from .NPC import NPC
from .base_class import Interactable
from JsonSerializable import JsonSerializable


class Dealer(NPC, Interactable, JsonSerializable):
    """A Dealer NPC that trades items with the player."""

    def __init__(self, description: str):
        """Initialize a Dealer with a description and inventory."""
        super().__init__(description)
        self._inventory = {"weapon upgrade": 15, "max HP potion": 20}

    def interact(self, player) -> None:
        """Offer a trade to the player."""
        message = (
            f"{self.description} says he has something you might like. "
            "Would you like to trade?"
        )
        print(message)

    def sell_item(self, player, item: str):
        """Sell an item to the player, updating money and stats."""
        price = self._inventory[item]
        if player.money >= price:
            player.money -= price
            print(f"You bought {item} for ${price}. "
                  f"Remaining money: ${player.money}")
            if item == "weapon upgrade":
                player.damage *= 1.2
                print(f"Your weapon was upgraded! New baseline "
                      f"damage: {player.damage}")
            elif item == "max HP potion":
                player.health = player._max_health
                print("Full health restored!")
        else:
            print(f" {item}. You need ${price} but have ${player.money}.")

    def toJSON(self) -> dict:
        """Serialize the Dealer object to a dictionary."""
        return {"description": self.description, "inventory": self._inventory}

    @classmethod
    def fromJSON(cls, data: dict):
        """Deserialize a Dealer object from a dictionary."""
        dealer = cls(data["description"])
        dealer._inventory = data["inventory"]
        return dealer
