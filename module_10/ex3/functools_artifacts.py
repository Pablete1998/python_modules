#!/usr/bin/env python3
"""
FuncMage Chronicles - Exercise 3: Ancient Library
Explore the functools module's treasures.
"""

import functools
import operator
from collections.abc import Callable
from typing import Any

# ─────────────────────────────────────────────────────────────
# MÓDULOS DE ESTE EJERCICIO:
#
# functools → herramientas para trabajar con funciones:
#   - reduce    → combina una lista en un único valor
#   - partial   → "pre-rellena" argumentos de una función
#   - lru_cache → memoriza resultados para no recalcularlos
#   - wraps     → preserva el nombre/docstring al decorar (ex4)
#   - singledispatch → ejecuta código diferente según el tipo
#
# operator → versiones funcionales de los operadores de Python:
#   - operator.add(a, b)  equivale a  a + b
#   - operator.mul(a, b)  equivale a  a * b
#   - No podemos usar lambda en reduce para max/min, así que
#     creamos nuestras propias funciones auxiliares.
# ─────────────────────────────────────────────────────────────


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers into a single value."""

    # Si la lista está vacía, devolvemos 0 directamente.
    if not spells:
        return 0

    # Mapeamos el string de operación a la función real del módulo operator.
    operations = {
        'add': operator.add,         # add(a, b) → a + b
        'multiply': operator.mul,    # mul(a, b) → a * b
    }

    # Para max y min, operator no tiene funciones directas que tomen
    # dos argumentos y devuelvan el mayor/menor, así que las definimos:
    def op_max(a: int, b: int) -> int:
        return a if a > b else b

    def op_min(a: int, b: int) -> int:
        return a if a < b else b

    operations['max'] = op_max
    operations['min'] = op_min

    # Si la operación no existe, lanzamos un error descriptivo.
    if operation not in operations:
        raise ValueError(f"Unknown operation: '{operation}'."
                         f" Use: add, multiply, max, min.")

    # functools.reduce(funcion, lista):
    # Aplica la función acumulativamente a los elementos de la lista
    # hasta reducirlos a un único valor.
    #
    # Ejemplo visual con 'add' y [10, 20, 30, 40]:
    #   paso 1: add(10, 20) → 30
    #   paso 2: add(30, 30) → 60
    #   paso 3: add(60, 40) → 100
    #   resultado: 100
    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create 3 specialized versions of a base enchantment function."""

    # base_enchantment tiene firma: (power: int, element: str, target: str)
    # functools.partial nos permite pre-rellenar algunos argumentos,
    # creando una nueva función que ya no los necesita.
    #
    # Ejemplo visual:
    #   base_enchantment(power=50, element='fire', target='Dragon')
    #
    #   fire_enchant = partial(base_enchantment, power=50, element='fire')
    #   fire_enchant(target='Dragon')  ← solo necesita target ahora
    #
    # Creamos 3 versiones, cada una pre-rellena con power=50 y su elemento.
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


# @functools.lru_cache es un decorador que guarda los resultados
# de llamadas anteriores en una caché.
# Si llamas memoized_fibonacci(10) dos veces, la segunda vez
# devuelve el resultado guardado SIN recalcular nada.
#
# Sin caché, fibonacci(35) haría millones de llamadas recursivas.
# Con caché, cada valor se calcula UNA SOLA VEZ.
@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number using memoization."""

    # Casos base: fib(0) = 0, fib(1) = 1
    if n <= 0:
        return 0
    if n == 1:
        return 1

    # Caso recursivo: fib(n) = fib(n-1) + fib(n-2)
    # Gracias a lru_cache, fib(n-1) y fib(n-2) no se recalculan
    # si ya fueron llamados antes.
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Create a single dispatch system that handles different spell types."""

    # @singledispatch crea una función que se comporta diferente
    # según el TIPO del primer argumento.
    # La función base maneja el caso por defecto (tipo desconocido).
    @functools.singledispatch
    def cast(spell) -> str:
        return "Unknown spell type"

    # @cast.register(tipo) registra una versión especializada
    # para ese tipo concreto.

    # Cuando el argumento es un int → hechizo de daño
    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    # Cuando el argumento es un str → encantamiento
    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    # Cuando el argumento es una list → multi-cast
    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    # Devolvemos el dispatcher, que ya tiene todas las versiones registradas.
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
