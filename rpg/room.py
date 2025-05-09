from .door import Door
from .NPC import NPC
from JsonSerializable import JsonSerializable
from typing import List


class Room(JsonSerializable):
    """Represents a room in the game containing NPCs and doors."""

    def __init__(self, description: str):
        """Initialize the room with a description, doors, and NPCs."""
        self.description: str = description
        self._doors: List[Door] = []
        self._NPCs: List[NPC] = []

    @property
    def doors(self) -> List[Door]:
        """Get the list of doors in the room."""
        return self._doors

    @doors.setter
    def doors(self, doors: List[Door]) -> None:
        """Set the list of doors in the room, ensuring it is a list."""
        if not isinstance(doors, list):
            raise ValueError("Doors must be a list of Door objects.")
        self._doors = doors

    @property
    def NPCs(self):
        """Get the list of NPCs in the room."""
        return self._NPCs

    @NPCs.setter
    def NPCs(self, NPCs: List[NPC]) -> None:
        """Set the list of NPCs in the room, ensuring it is a list."""
        if not isinstance(NPCs, list):
            raise ValueError("NPCs must be a list of NPC objects.")
        self._NPCs = NPCs

    def add_door(self, description: str, destination) -> None:
        """Add a door leading to another room."""
        door = Door(description, destination)
        self._doors.append(door)

    def add_npc(self, npc: NPC) -> None:
        """Add an NPC to the room."""
        self._NPCs.append(npc)

    def inspect(self) -> None:
        """Print the description of the room."""
        print(f"You are in the {self.description}.")

    def toJSON(self):
        """Serialize room object to a JSON-compatible dict."""
        return {
            "description": self.description,
            "npcs": [npc.toJSON() for npc in self._NPCs],
        }

    @classmethod
    def fromJSON(cls, data):
        """Deserialize room object from JSON-compatible dict."""
        room = cls(data["description"])
        room.NPCs = [NPC.fromJSON(npc_data) for npc_data in data["npcs"]]
        return room
