#!/usr/bin/env python3

from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.healing import HealCapability
from ex1.transforming import TransformCapability


class BattleStrategy(ABC):

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> str:
        return creature.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, TransformCapability):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )
        return (
            f"{creature.transform()}\n{creature.attack()}\n{creature.revert()}"
        )


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        if isinstance(creature, HealCapability):
            return True
        return False

    def act(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            raise ValueError(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
            )
        return f"{creature.attack()}\n{creature.heal()}"
