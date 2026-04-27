"""
FuncMage Chronicles - Exercise 1: Higher Realm
Discover the power of higher-order functions.
"""

from collections.abc import Callable


def spell_combiner(
    spell1: Callable[[str, int], str],
    spell2: Callable[[str, int], str]
) -> Callable[[str, int], tuple[str, str]]:
    """Return a new spell that casts both spells and returns both results."""
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(
    base_spell: Callable[[str, int], str],
    multiplier: int
) -> Callable[[str, int], str]:
    """Return a new spell with power multiplied before casting."""
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(
    condition: Callable[[str, int], bool],
    spell: Callable[[str, int], str]
) -> Callable[[str, int], str]:
    """Return a spell that only casts if the condition is True."""
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(
    spells: list[Callable[[str, int], str]]
) -> Callable[[str, int], list[str]]:
    """Return a function that casts all spells and returns all results."""
    def cast_all(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return cast_all


def fireball(target: str, power: int) -> str:
    """Cast a fireball at the target."""
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    """Heal the target."""
    return f"Heal restores {target} for {power} HP"


def shield(target: str, power: int) -> str:
    """Shield the target."""
    return f"Shield protects {target} with {power} defense"


if __name__ == "__main__":
    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon", 50)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Dragon', 10)}")
    print(f"Amplified: {mega_fireball('Dragon', 10)}")

    print("\nTesting conditional caster...")
    strong_enough: Callable[[str, int], bool] = (
        lambda target, power: power >= 50
    )
    conditional_fireball = conditional_caster(strong_enough, fireball)
    print(conditional_fireball("Dragon", 30))
    print(conditional_fireball("Dragon", 60))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    results = sequence("Dragon", 50)
    for r in results:
        print(r)
