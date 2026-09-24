#!/usr/bin/env python3

from typing import Callable, Any
from data_generator import FuncMageDataGenerator


def mage_counter() -> Callable[[], int]:
    """Create a counting closure starting from 1."""
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """Create a power accumulator starting with initial_power."""
    total = initial_power

    def accumulate(power: int) -> int:
        nonlocal total
        total += power
        return total
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """Create enchantment functions formatting 'type item'."""

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable[..., Any]]:
    """Create a private memory storage system."""
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print(f"counter_a call 3: {counter_a()}")
    print(f"counter_b call 2: {counter_b()}")

    print("\nTesting spell accumulator...")
    initial_powers = [random_val := 100]
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")
    print(f"Base 100, add 30: {acc(30)}")

    print("\nTesting enchantment factory...")
    enchantment_types = FuncMageDataGenerator.ENCHANTMENT_TYPES[:2]
    items = FuncMageDataGenerator.generate_enchantment_items(2)

    flaming = enchantment_factory(enchantment_types[0])
    frozen = enchantment_factory(enchantment_types[1])
    print(flaming(items[0]))
    print(frozen(items[1]))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
