from .NPC import NPC
import random
from JsonSerializable import JsonSerializable
from typing import Dict, Any


class Enemy(NPC, JsonSerializable):
    """An enemy NPC that can attack the player."""

    def __init__(self, description: str, health: int, damage: int):
        """Initialize an Enemy with a description, health, and damage."""
        super().__init__(description)
        self._health = health
        self._damage = damage

    @property
    def health(self) -> int:
        """Return the health of the enemy."""
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """Set the health of the enemy, ensuring it doesn't go below 0."""
        if value < 0:
            self._health = 0
        else:
            self._health = value

    @property
    def damage(self) -> int:
        """Return the damage of the enemy."""
        return self._damage

    @damage.setter
    def damage(self, value: int) -> None:
        """Set the damage of the enemy, ensuring it's non-negative."""
        if value < 0:
            raise ValueError("Damage cannot be negative.")
        self._damage = value

    def attack(self, player) -> None:
        """Attack the player and deal random damage."""
        min_damage: int = int(self._damage * 0.9)
        max_damage: int = int(self._damage * 1.1)
        actual_damage: int = random.randint(min_damage, max_damage)

        hit_chance: float = random.random()
        if hit_chance < 0.2:
            print(f"{self.description}'s attack missed!")
            return

        crit_chance: float = random.random()
        if crit_chance < 0.1:
            actual_damage = int(actual_damage * 1.5)
            print(
                f"Critical hit! {self.description} deals "
                f"{actual_damage} damage to {player.name}!"
            )
        else:
            print(
                f"{self.description} attacks {player.name} for "
                f"{actual_damage} damage."
            )

        player.health -= actual_damage

    def interact(self, player) -> None:
        """Start combat with the player."""
        print(f"{self.description} is not looking like he wants to make "
              f"friends. It's time for a fight!")

    def toJSON(self) -> Dict[str, Any]:
        """Serialize the Enemy object to a dictionary."""
        return {
            "description": self.description,
            "health": self._health,
            "damage": self._damage,
        }

    @classmethod
    def fromJSON(cls, data: Dict[str, Any]):
        """Deserialize an Enemy object from a dictionary."""
        return cls(data["description"], data["health"], data["damage"])
