from .base_class import Inspectable, Interactable
from JsonSerializable import JsonSerializable
from typing import Dict, Any
import random


class NPC(Inspectable, Interactable, JsonSerializable):
    def __init__(self, description: str):
        self.description: str = description

    def inspect(self) -> None:
        print(f"You see: {self.description}")

    def interact(self, player) -> None:
        responses = [
            f"{self.description} glances at {player.name} briefly and then "
            f"goes back to what they were doing.",
            f"{self.description} gives {player.name} a cold shoulder and "
            f"mumbles something under their breath.",
            f"{self.description} ignores {player.name}, clearly "
            f"preoccupied with something else.",
            f"{self.description} waves {player.name} off, signaling that "
            f"they're not in the mood to chat.",
            f"{self.description} sighs and says, 'Not now, {player.name}. "
            f"I’m busy.'",
        ]

        message: str = random.choice(responses)
        print(message)

    def toJSON(self) -> Dict[str, Any]:
        return {"description": self.description}

    @classmethod
    def fromJSON(cls, data: Dict[str, Any]):
        return cls(data["description"])
