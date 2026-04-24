"""
FuncMage Chronicles - Exercise 1: Higher Realm
Discover the power of higher-order functions.
"""

# Importamos Callable de collections.abc (el PDF lo exige así,
# NO desde typing).
# Callable es simplemente un tipo que significa "esto es una función".
# Lo usamos en los type hints para decir "este argumento es una función".

from collections.abc import Callable

# ─────────────────────────────────────────────────────────────
# ¿QUÉ ES UNA FUNCIÓN DE ORDEN SUPERIOR?
#
# Es una función que:
#   - Recibe otras funciones como argumento, Y/O
#   - Devuelve una función como resultado
#
# Ejemplo mental:
#   def aplicar(funcion, valor):   ← recibe una función
#       return funcion(valor)      ← la ejecuta
#
# En este ejercicio, TODAS las funciones son de orden superior.
# ─────────────────────────────────────────────────────────────


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a new spell that casts both spells and returns both results."""

    # Recibimos dos funciones (spell1 y spell2) y devolvemos UNA NUEVA.
    # La función nueva, combined_spell, llama a las dos con los mismos
    # argumentos y devuelve los dos resultados juntos en una tupla.
    #
    # Ejemplo visual:
    #   fireball('Dragon', 50) → 'Fireball hits Dragon for 50'
    #   heal('Dragon', 50)     → 'Heal restores Dragon for 50 HP'
    #
    #   combined = spell_combiner(fireball, heal)
    #   combined('Dragon', 50) → ('Fireball hits Dragon for 50',
    #                              'Heal restores Dragon for 50 HP')

    def combined_spell(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))

    return combined_spell   # ← devolvemos la función, SIN llamarla


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a new spell with power multiplied before casting."""

    # Recibimos un hechizo y un multiplicador.
    # Devolvemos un hechizo nuevo que, antes de ejecutarse,
    # multiplica el power por el multiplicador.
    #
    # Ejemplo visual:
    #   fireball('Dragon', 10) → 'Fireball hits Dragon for 10'
    #
    #   mega = power_amplifier(fireball, 3)
    #   mega('Dragon', 10) → llama fireball('Dragon', 30)
    #                      → 'Fireball hits Dragon for 30'
    #
    # La función interna amplified_spell "recuerda" base_spell y multiplier
    # gracias al closure (lo veremos más en el ejercicio 2).

    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only casts if the condition is True."""

    # Recibimos una condición (función que devuelve True/False)
    # y un hechizo.
    # Devolvemos un hechizo nuevo que primero comprueba la condición
    # con los mismos argumentos, y solo lanza el hechizo si es True.
    #
    # Ejemplo visual:
    #   condicion = lambda target, power: power >= 50
    #   hechizo = fireball
    #
    #   caster = conditional_caster(condicion, hechizo)
    #   caster('Dragon', 30) → condición False → 'Spell fizzled'
    #   caster('Dragon', 60) → condición True  → 'Fireball hits Dragon for 60'

    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that casts all spells and returns all results."""

    # Recibimos una LISTA de hechizos.
    # Devolvemos una función que los lanza TODOS con los mismos argumentos
    # y devuelve una lista con todos los resultados.
    #
    # Ejemplo visual:
    #   sequence = spell_sequence([fireball, heal, shield])
    #   sequence('Dragon', 50) → [
    #       'Fireball hits Dragon for 50',
    #       'Heal restores Dragon for 50 HP',
    #       'Shield protects Dragon for 50'
    #   ]

    def cast_all(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]

    return cast_all


# ─────────────────────────────────────────────────────────────
# HECHIZOS DE EJEMPLO
# Siguen el contrato del PDF: spell(target: str, power: int) -> str
# ─────────────────────────────────────────────────────────────

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
    # spell_combiner devuelve una función nueva — la guardamos en combined
    combined = spell_combiner(fireball, heal)
    # Ahora llamamos a combined como si fuera un hechizo normal
    result = combined("Dragon", 50)
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original = fireball("Dragon", 10)
    amplified = mega_fireball("Dragon", 10)
    # El power original era 10, el amplificado es 10*3 = 30
    print(f"Original: {original}")
    print(f"Amplified: {amplified}")

    print("\nTesting conditional caster...")
    # La condición: solo lanzar si el poder es >= 50
    strong_enough = lambda target, power: power >= 50  # noqa: E731
    conditional_fireball = conditional_caster(strong_enough, fireball)
    print(conditional_fireball("Dragon", 30))   # → Spell fizzled
    print(conditional_fireball("Dragon", 60))   # → Fireball hits...

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    results = sequence("Dragon", 50)
    for r in results:
        print(r)
