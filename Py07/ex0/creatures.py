#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Creature(ABC):
    """Abstract base class for all Creatures."""

    def __init__(self, name: str, creature_type: str) -> None:
        self.name = name
        self.type = creature_type

    def describe(self) -> str:
        """Concrete method that returns creature description"""
        return f"{self.name} is a {self.type} type Creature"
    
    @abstractmethod
    def attack(self) -> str:
        """Abstract method that returns creature attack"""
        pass


class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"

class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"

class Aquabub(Creature):
    def __init__(self) -> None:
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"

class Torragon(Creature):
    def __init__(self) -> None:
        super().__init__("Torragon", "Water")

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"
