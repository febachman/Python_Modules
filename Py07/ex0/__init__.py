#!/usr/bin/env python3

#  ex0/__init__.py: Turns the folder into a Python package. Per instructions, it must restrict exports to only the factory classes (e.g., FlameFactory, AquaFactory, and CreatureFactory), preventing direct imports of concrete creatures like Flameling or Aquabub.

from .factories import CreatureFactory, FlameFactory, AquaFactory

__all__ = ["CreatureFactory", "FlameFactory", "AquaFactory"]

# Usage: Exposes only the factories to external scripts like battle.py, satisfying the requirement that concrete creatures cannot be imported directly from the package.
