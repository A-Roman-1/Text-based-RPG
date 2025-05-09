from .base_class import Inspectable, Interactable
from JsonSerializable import JsonSerializable
from typing import Dict, Any


class Door(Inspectable, Interactable, JsonSerializable):
    """A Door that connects two rooms and can be interacted with."""

    def __init__(self, description: str, leads_to):
        """Initialize the Door with a description and destination."""
        self.description = description
        self.leads_to = leads_to

    def inspect(self) -> None:
        """Describe the door and where it leads."""
        print(f"There is a {self.description} leading to "
              f"{self.leads_to.description}.")

    def interact(self, player) -> None:
        """Move the player to the room the door leads to."""
        print(f"You go through the {self.description}.")
        player.room = self.leads_to

    def toJSON(self) -> Dict[str, Any]:
        """Serialize the Door object to a dictionary."""
        return {
            "description": self.description,
            "leads_to": self.leads_to.toJSON(),
        }

    @classmethod
    def fromJSON(cls, data: Dict[str, Any]):
        """Deserialize a Door object from a dictionary."""
        from .room import Room

        leads_to = Room.fromJSON(data["leads_to"])
        return cls(data["description"], leads_to)
