#!/usr/bin/env python3

#  ex0/creatures.py: Houses the abstract Creature base class (defining name, type, abstract attack, and concrete describe methods) along with the concrete creature implementations (Flameling, Pyrodon, Aquabub, and Torragon).

from abc import ABC, abstractmethod
from typing import Optional

class Creatures(ABC):
    """Abstract class hat holds attributes for name and type of the Creature"""

    def __init__(self) -> None:
        self._storage: List[Tuple[int, str]] = []
        self._rank: int = 0

    @abstractmethod
    def attack():

	def describe():

class Flameling(Creatures):

class Pyrodon(Creatures):

class Aquabub(Creatures):

class Torragon(Creatures):
