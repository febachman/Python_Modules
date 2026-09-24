#!/usr/bin/env python3

import functools
import operator
import random
from typing import Callable, Any
from data_generator import FuncMageDataGenerator


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce spell powers using functools.reduce and operator module."""
    if not spells:
        return 0

    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
    }

    if operation in ("max", "min"):
        func = max if operation == "max" else min
        return int(func(spells))

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")

    return int(functools.reduce(ops[operation], spells))


def base_enchantment(power: int, element: str, target: str) -> str:
    """Base enchantment function to be partially applied."""
    return f"{element.capitalize()} enchantment of power {power} on {target}"


def partial_enchanter(
    base_func: Callable[..., str]
) -> dict[str, Callable[..., Any]]:
    """Create partial applications pre-filling power=50 and elements."""
    elements = ["fire", "ice", "lightning"]
    enchanters: dict[str, Callable[..., Any]] = {}

    for elem in elements:
        # Pre-fills power=50 and element=elem
        enchanters[elem] = functools.partial(base_func, 50, elem)

    return enchanters


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number with lru_cache memoization."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Create a single dispatch system handling different types."""
    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list[str]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    spell_powers = FuncMageDataGenerator.generate_spell_powers(5)
    print(f"Generated spell powers: {spell_powers}")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print(f"Min: {spell_reducer(spell_powers, 'min')}")

    print("\nTesting memoized fibonacci...")
    fib_tests = [0, 1, random.randint(8, 12), random.randint(13, 18)]
    for n in fib_tests:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting partial enchanter...")
    enchanters = partial_enchanter(base_enchantment)
    items = FuncMageDataGenerator.generate_enchantment_items(2)
    print(enchanters['fire'](items[0]))
    print(enchanters['ice'](items[1]))

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()

    # 1. Test: int type (magical power)
    dynamic_power = FuncMageDataGenerator.generate_spell_powers(1)[0]
    print(dispatcher(dynamic_power))

    # 2. Test: str type (magical name)
    dynamic_spell = FuncMageDataGenerator.generate_spells(1)[0]
    print(dispatcher(dynamic_spell))

    # 3. Test: list type (multiple spells)
    dynamic_multicast = FuncMageDataGenerator.generate_spells(3)
    print(dispatcher(dynamic_multicast))

    # 4. Test: unkown type (fallback)
    print(dispatcher(3.14))
