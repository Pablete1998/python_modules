"""
FuncMage Chronicles - Exercise 4: Master's Tower
Create powerful decorators and class methods.
"""

import time
import functools
from collections.abc import Callable
from typing import Any, TypeVar

F = TypeVar('F', bound=Callable[..., Any])


def spell_timer(func: F) -> F:
    """Decorator that measures and prints the execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper  # type: ignore[return-value]


def power_validator(min_power: int) -> Callable[[F], F]:
    """Decorator factory that validates the power level before casting."""
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper  # type: ignore[return-value]
    return decorator


def retry_spell(max_attempts: int) -> Callable[[F], F]:
    """Decorator factory that retries a function if it raises an exception."""
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying..."
                          f" (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper  # type: ignore[return-value]
    return decorator


class MageGuild:
    """A guild that manages mages and their spell casting."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check if a mage name is valid."""
        return (len(name) >= 3
                and all(c.isalpha() or c.isspace() for c in name))

    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with power validation."""
        if power < 10:
            return "Insufficient power for this spell"
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball_timed() -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball_timed()
    print(f"Result: {result}")

    print("\nTesting power validator...")

    @power_validator(20)
    def thunder(power: int, target: str) -> str:
        return f"Thunder strikes {target} for {power} damage"

    print(thunder(10, "Dragon"))
    print(thunder(50, "Dragon"))

    print("\nTesting retrying spell...")
    attempt_count = [0]

    @retry_spell(3)
    def always_fails() -> str:
        raise Exception("Always fails")

    @retry_spell(3)
    def unstable_spell() -> str:
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise Exception("Spell unstable!")
        return "Waaaaaaagh spelled !"

    print(always_fails())
    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("X2"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
