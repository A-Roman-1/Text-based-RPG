import random
from JsonSerializable import JsonSerializable
from .room import Room
from typing import Dict, Any


class Player(JsonSerializable):
    """Represents the player character in the game."""
    def __init__(self, name: str, room: Room, health: int = 100,
                 damage: int = 10):
        """Initialize the player with name, room, health, damage, and money."""
        self._name: str = name
        self._room: Room = room
        self._max_health: int = health
        self._health: int = health
        self._damage: int = damage
        self._money: int = 10

    def inspect_current_room(self) -> None:
        """Describe the current room the player is in."""
        print(f"{self._name} sees {self._room.description}")

    def attack(self, enemy) -> None:
        """Perform an attack on an enemy, considering hit chance and
        critical hits."""
        min_damage: int = int(self._damage * 0.9)
        max_damage: int = int(self._damage * 1.1)
        actual_damage: int = random.randint(min_damage, max_damage)
        hit_chance: float = random.random()
        if hit_chance < 0.2:
            print(f"{self._name}'s attack missed!")
            return

        crit_chance: float = random.random()
        if crit_chance < 0.1:
            actual_damage = int(actual_damage * 1.5)
            print(
                f"Critical hit! {self._name} deals {actual_damage} damage to "
                f"{enemy.description}!"
            )
        else:
            print(
                f"{self._name} attacks {enemy.description} for "
                f"{actual_damage} damage."
            )
        enemy.health -= actual_damage

    @property
    def name(self) -> str:
        """Get the player's name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set player's name."""
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def room(self) -> Room:
        """Getter for room"""
        return self._room

    @room.setter
    def room(self, value: Room) -> None:
        """Setter for room"""
        if not isinstance(value, Room):
            raise ValueError("Room must be a valid Room object.")
        self._room = value

    @property
    def health(self) -> int:
        """Getter for player HP"""
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """Setter for player HP"""
        if value < 0:
            self._health = 0
        elif value > self._max_health:
            self._health = self._max_health
        else:
            self._health = value

    @property
    def damage(self) -> int:
        """Getter for player's baseline damage"""
        return self._damage

    @damage.setter
    def damage(self, value: int) -> None:
        """Setter for player's baseline damage"""
        if value < 0:
            raise ValueError("Damage cannot be negative.")
        self._damage = value

    @property
    def money(self) -> int:
        """"Getter for player's money amount"""
        return self._money

    @money.setter
    def money(self, value: int) -> None:
        """Setter for player's money amount"""
        if value < 0:
            raise ValueError("Money cannot be negative.")
        self._money = value

    def is_alive(self) -> bool:
        """Function that checks if player is still alive"""
        return self._health > 0

    def toJSON(self) -> Dict[str, Any]:
        """Serialize player to a JSON-compatible dictionary."""
        return {
            "name": self._name,
            "room": self._room.toJSON(),
            "health": self._health,
            "damage": self._damage,
            "money": self._money,
        }

    @classmethod
    def fromJSON(cls, data: Dict[str, Any]) -> "Player":
        """Deserialize player object from a JSON-compatible dictionary."""
        room: Room = Room.fromJSON(data["room"])
        player: Player = cls(data["name"], room, data["health"],
                             data["damage"])
        player.money = data.get("money", 0)
        return player
