#!/usr/bin/env python3

# ex0/factories.py: Contains the abstract CreatureFactory class (create_base and create_evolved) and its concrete implementations (FlameFactory and AquaFactory).

from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon
