"""
FuncMage Chronicles - Exercise 3: Ancient Library
Explore the functools module's treasures.
"""

import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers into a single value."""
    if not spells:
        return 0

    def op_max(a: int, b: int) -> int:
        return a if a > b else b

    def op_min(a: int, b: int) -> int:
        return a if a < b else b

    operations: dict[str, Callable[[int, int], int]] = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': op_max,
        'min': op_min,
    }

    if operation not in operations:
        raise ValueError(f"Unknown operation: '{operation}'."
                         f" Use: add, multiply, max, min.")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(
    base_enchantment: Callable[..., str]
) -> dict[str, Callable[..., str]]:
    """Create 3 specialized versions of a base enchantment function."""
    fire_enchant = functools.partial(base_enchantment, power=50,
                                     element='fire')
    ice_enchant = functools.partial(base_enchantment, power=50,
                                    element='ice')
    lightning_enchant = functools.partial(base_enchantment, power=50,
                                          element='lightning')
    return {
        'fire': fire_enchant,
        'ice': ice_enchant,
        'lightning': lightning_enchant
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Create a single dispatch system that handles different spell types."""
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return cast


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return (f"{element.capitalize()} enchantment"
                f" on {target} (power {power})")

    enchants = partial_enchanter(base_enchant)
    print(enchants['fire'](target='Sword'))
    print(enchants['ice'](target='Shield'))
    print(enchants['lightning'](target='Staff'))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("fireball"))
    print(dispatcher(["fire", "ice", "x"]))
    print(dispatcher(3.14))
