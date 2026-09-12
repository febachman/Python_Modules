#!/usr/bin/env python3

# ex0/factories.py: Contains the abstract CreatureFactory class (create_base and create_evolved) and its concrete implementations (FlameFactory and AquaFactory).

from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon

class CreatureFactory(ABC):
    """Abstract base class for Creature creation and evolution."""
    
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragon()
