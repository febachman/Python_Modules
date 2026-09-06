#!/usr/bin/env python3

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str):
    allowed = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()
    is_valid = any(item.lower() in ingredients_lower for item in allowed)
    return "VALID" if is_valid else "INVALID"
