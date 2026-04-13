#!/usr/bin/env python3

from alchemy.grimoire.light_validator import validate_ingredients


def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    validation = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation})"
