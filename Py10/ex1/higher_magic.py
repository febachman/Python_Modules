#!/usr/bin/env python3

from collections.abc import Callable
from data_generator import FuncMageDataGenerator


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    """Combine two spells into one that returns a tuple of both results."""
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined_spell


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    """Return a new spell where the power is multiplied before casting."""
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    """Cast spell conditionally; if condition fails, return 'Spell fizzled'."""
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    """Executes all spells in order and returns a list of results."""
    def sequential_spell(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequential_spell


if __name__ == "__main__":
    print("=== Higher Realm ===")

    # Data from data_generator
    targets = FuncMageDataGenerator.generate_artifacts(2)
    target_name = "Dragon"

    # Spells for example
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def lightning(target: str, power: int) -> str:
        return f"Lightning zaps {target} with {power} shock"

    print("\n--- Testing spell_combiner ---")
    combined = spell_combiner(fireball, heal)
    print("Combined result:", combined(target_name, 25))

    print("\n--- Testing power_amplifier ---")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original (10 power):", fireball("Goblin", 10))
    print("Amplified (10 * 3 power):", mega_fireball("Goblin", 10))

    print("\n--- Testing conditional_caster ---")

    # Condition: only cast spell if power >= 30
    def is_strong(t: str, p: int) -> bool:
        return p >= 30

    guarded_lightning = conditional_caster(is_strong, lightning)
    print("Casting with low power (15):", guarded_lightning("Wizard", 15))
    print("Casting with high power (40):", guarded_lightning("Wizard", 40))

    print("\n--- Testing spell_sequence ---")
    sequence = spell_sequence([fireball, heal, lightning])
    results = sequence("Knight", 20)
    print("Sequence results:")
    for res in results:
        print(f" -> {res}")
