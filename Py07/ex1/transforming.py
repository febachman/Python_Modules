#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex0 import CreatureFactory


class TransformCapability(ABC):
    """Abstract class for transforming capability with persistent state"""

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self.name} returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return f"{self.name} stabilizes its form."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
