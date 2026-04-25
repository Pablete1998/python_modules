"""
FuncMage Chronicles - Exercise 2: Memory Depths
Understand lexical scoping and closures.
"""

from collections.abc import Callable

# ─────────────────────────────────────────────────────────────
# ¿QUÉ ES UN CLOSURE?
#
# Un closure es una función que "recuerda" las variables del
# entorno donde fue creada, incluso después de que ese entorno
# haya dejado de existir.
#
# Ejemplo mental:
#   def outer():
#       x = 10           ← variable en el entorno de outer
#       def inner():
#           return x     ← inner "recuerda" x aunque outer haya terminado
#       return inner
#
#   f = outer()   ← outer termina, pero x sigue viva dentro de f
#   f()           → 10
#
# ¿Por qué nonlocal y no global?
#   - global → accede a variables del nivel más alto del módulo.
#     Rompe la pureza funcional, cualquier función puede tocarlo.
#   - nonlocal → accede solo a la variable del scope inmediatamente
#     superior (la función que la envuelve). Más controlado y seguro.
# ─────────────────────────────────────────────────────────────


def mage_counter() -> Callable:
    """Return a function that counts how many times it has been called."""

    # count vive aquí, en el scope de mage_counter.
    # La función interna 'counter' la recuerda gracias al closure.
    count = 0

    def counter() -> int:
        # nonlocal le dice a Python: "el 'count' que quiero modificar
        # no es uno nuevo local mío, es el del scope superior".
        # Sin nonlocal, Python crearía un 'count' local nuevo y daría error.
        nonlocal count
        count += 1
        return count

    # Devolvemos la función, no la llamamos.
    # Cada vez que llames a mage_counter() obtienes un counter
    # INDEPENDIENTE con su propio 'count' en 0.
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    """Return a function that accumulates power with each call."""

    # total empieza en initial_power (el valor que nos pasan).
    # Cada llamada a la función interna le suma más poder.
    total = initial_power

    def add_power(amount: int) -> int:
        # nonlocal para poder modificar 'total' del scope superior.
        nonlocal total
        total += amount
        return total

    # Ejemplo visual:
    #   acc = spell_accumulator(100)
    #   acc(20) → total = 100+20 = 120
    #   acc(30) → total = 120+30 = 150  ← recuerda el estado anterior
    return add_power


def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that applies a specific enchantment to any item."""

    # enchantment_type queda "atrapado" en el closure.
    # La función interna lo recuerda sin necesidad de nonlocal
    # porque solo lo LEE, no lo modifica.
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    # Ejemplo visual:
    #   flaming = enchantment_factory("Flaming")
    #   flaming("Sword")  → "Flaming Sword"
    #   flaming("Shield") → "Flaming Shield"
    #
    #   frozen = enchantment_factory("Frozen")
    #   frozen("Shield")  → "Frozen Shield"
    return enchant


def memory_vault() -> dict[str, Callable]:
    """Return a dict with store and recall functions sharing storage."""

    # _storage es el almacenamiento privado compartido entre store y recall.
    # Ninguna función externa puede tocarlo directamente — solo a través
    # de store y recall. Eso es encapsulación funcional.
    _storage: dict = {}

    def store(key: str, value) -> None:
        # Solo lee _storage (es un dict, lo modifica internamente),
        # no necesita nonlocal porque no reasignamos _storage,
        # solo llamamos a su método __setitem__.
        _storage[key] = value

    def recall(key: str):
        # dict.get devuelve el valor si existe, o el segundo argumento
        # si no existe. Aquí devolvemos "Memory not found" si la clave
        # no está en el almacenamiento.
        return _storage.get(key, "Memory not found")

    # Devolvemos ambas funciones dentro de un dict.
    # Las dos comparten el mismo _storage gracias al closure.
    return {'store': store, 'recall': recall}


if __name__ == "__main__":

    print("Testing mage counter...")
    # Dos contadores completamente independientes
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")   # → 1
    print(f"counter_a call 2: {counter_a()}")   # → 2
    print(f"counter_b call 1: {counter_b()}")   # → 1 (independiente)

    print("\nTesting spell accumulator...")
    acc = spell_accumulator(100)
    print(f"Base 100, add 20: {acc(20)}")   # → 120
    print(f"Base 100, add 30: {acc(30)}")   # → 150

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))    # → Flaming Sword
    print(frozen("Shield"))    # → Frozen Shield

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
