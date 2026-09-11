#!/usr/bin/env python3

#  absolute import (root)
from elements import create_fire
#  relative import (alchemy/elements)
from ..elements import create_air
#  relative import (alchemy/potions)
from ..potions import strength_potion


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}' mixed with '{create_fire()}'"
    )
