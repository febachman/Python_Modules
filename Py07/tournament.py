#!/usr/bin/env python3

from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy, NormalStrategy, AggressiveStrategy, DefensiveStrategy
)
from typing import List, Tuple


def tournament(
    opponents: List[Tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            print("\n* Battle *")
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            c1 = factory1.create_base()
            c2 = factory2.create_base()

            try:
                print(c1.describe())
                print("vs.")
                print(c2.describe())
                print("now fight!")

                print(strategy1.act(c1))
                print(strategy2.act(c2))
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    print("Tournament 0 (basic)")
    print("[(Flameling+Normal), (Healing+Defensive)]")
    opponents_0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    tournament(opponents_0)

    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive)]")
    opponents_1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    tournament(opponents_1)

    print("\nTournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive)]")
    opponents_2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    tournament(opponents_2)
