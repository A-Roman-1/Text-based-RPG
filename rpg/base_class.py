from abc import ABC, abstractmethod


class Inspectable(ABC):
    """Abstract class for inspectable objects"""
    @abstractmethod
    def inspect(self) -> None:
        pass


class Interactable(ABC):
    """Abstract class for interactable objects"""
    @abstractmethod
    def interact(self, Player) -> None:
        pass


class Attackable(ABC):
    """Abstract class for objects which can combat"""
    @abstractmethod
    def Attack(self, subject) -> None:
        pass
