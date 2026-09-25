#!/usr/bin/env python3

import time
import functools
import re
from typing import Callable, Any
from data_generator import FuncMageDataGenerator


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Time execution decorator measuring execution time"""

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = end_time - start_time
        print(f"Spell completed in {duration:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable[..., Any]:
    """Parameterized validation decorator for power levels"""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')
            if power is None and len(args) >= 3:
                power = args[2]
            elif power is None and len(args) >= 2:
                power = args[1]

            if power is not None and power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    """Decorator that retries failed spells up to max_attempts times"""
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            "Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )
                    else:
                        return (
                            "Spell casting failed after "
                            f"{max_attempts} attempts\n"
                            "Waaaaaaagh spelled !"
                        )
        return wrapper
    return decorator


class MageGuild:
    """Demonstrate staticmethod and instance methods with decorators"""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Validate if name is >= 3 chars & contains only letters/spaces"""
        if len(name) < 3:
            return False
        return bool(re.match(r"^[A-Za-z\s]+$", name))

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell using the power_validator decorator"""
        return f"Successfully cast {spell_name} with {power} power"


# Aux functions
@spell_timer
def fireball() -> str:
    """Sample function for testing spell_timer decorator"""
    time.sleep(0.1)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    """Sample function that fails to test retry_spell decorator"""
    raise ValueError("Magical instability!")


def main() -> None:
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting retrying spell...")
    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()

    mage_names = FuncMageDataGenerator.MAGE_NAMES[:2]
    invalid_names = ["Jo", "Alex123"]

    print(MageGuild.validate_mage_name(mage_names[0]))
    print(MageGuild.validate_mage_name(invalid_names[0]))

    spell_name = FuncMageDataGenerator.generate_spells(1)[0].capitalize()
    print(guild.cast_spell(spell_name, 15))
    print(guild.cast_spell(spell_name, 5))


if __name__ == "__main__":
    main()
