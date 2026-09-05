#!/usr/bin/env python3

from elements import create_fire # absolute import (root)
from ..elements import create_air # relative import (alchemy/elements)
from ..potions import strength_potion # relative import (alchemy/potions)

def lead_to_gold():
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}' mixed with '{create_fire()}'"
    )
