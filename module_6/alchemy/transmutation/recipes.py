#!/usr/bin/env python3

from alchemy.potions import strength_potion  # absolute import
from ..elements import create_air  # relative import
import elements  # para create_fire


def lead_to_gold() -> str:
    return (
        f"Recipe transmuting Lead to Gold: brew '{create_air()}'"
        f" and '{strength_potion()}' mixed with '{elements.create_fire()}'"
    )
