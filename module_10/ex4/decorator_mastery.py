#!/usr/bin/env python3
"""
FuncMage Chronicles - Exercise 4: Master's Tower
Create powerful decorators and class methods.
"""

import time
import functools
from collections.abc import Callable

# ─────────────────────────────────────────────────────────────
# ¿QUÉ ES UN DECORADOR?
#
# Un decorador es una función que ENVUELVE a otra función
# para añadirle comportamiento extra sin modificarla.
#
# Sintaxis con @:
#   @mi_decorador
#   def mi_funcion():
#       ...
#
# Es exactamente igual a escribir:
#   mi_funcion = mi_decorador(mi_funcion)
#
# El decorador recibe la función original, crea una función
# nueva que hace "algo antes/después", y la devuelve.
#
# functools.wraps es OBLIGATORIO dentro del decorador:
# sin él, la función envuelta pierde su __name__ y __doc__,
# lo que rompe debugging, documentación y otros decoradores.
# ─────────────────────────────────────────────────────────────


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints the execution time of a function."""

    # @functools.wraps(func) copia el nombre, docstring y metadata
    # de la función original a la función wrapper.
    # Sin esto: wrapper.__name__ sería 'wrapper' en vez de 'fireball'.
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # *args y **kwargs capturan CUALQUIER argumento que reciba la función.
        # Así el decorador funciona con funciones de cualquier firma.
        print(f"Casting {func.__name__}...")
        start = time.time()           # guardamos el tiempo de inicio
        result = func(*args, **kwargs)  # llamamos a la función original
        end = time.time()             # guardamos el tiempo de fin
        elapsed = end - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result   # devolvemos el resultado original sin alterarlo

    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that validates the power level before casting."""

    # Este es un decorador PARAMETRIZADO (fábrica de decoradores).
    # Tiene una capa extra: power_validator(10) devuelve un decorador,
    # y ese decorador envuelve la función.
    #
    # Flujo:
    #   @power_validator(10)       ← llama a power_validator(10)
    #   def cast_spell(power, ...  ←   que devuelve 'decorator'
    #                              ←   que envuelve cast_spell
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # El PDF dice: "Applied on a standalone function whose
            # first argument is power."
            # args[0] es el primer argumento posicional → power.
            power = args[0]
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator factory that retries a function if it raises an exception."""

    # Otro decorador parametrizado. Si la función lanza una excepción,
    # la reintenta hasta max_attempts veces.
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    # Intentamos llamar a la función.
                    return func(*args, **kwargs)
                except Exception:
                    # Si falla, imprimimos el aviso y continuamos el bucle.
                    print(f"Spell failed, retrying..."
                          f" (attempt {attempt}/{max_attempts})")
            # Si agotamos todos los intentos sin éxito, devolvemos el mensaje.
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """A guild that manages mages and their spell casting."""

    # @staticmethod: método que NO recibe 'self' ni 'cls'.
    # Pertenece a la clase por organización, pero no necesita
    # acceder a ningún dato de la instancia ni de la clase.
    # Se llama como MageGuild.validate_mage_name("Alex")
    # o también como guild.validate_mage_name("Alex").
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Check if a mage name is valid (>=3 chars, only letters/spaces)."""
        # all() devuelve True si TODOS los elementos de la secuencia son True.
        # Comprobamos que cada carácter sea letra o espacio.
        return len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name)

    # Aplicamos power_validator como decorador con min_power=10.
    # Pero hay un detalle: power_validator espera power como args[0],
    # y en un método de instancia args[0] es 'self'.
    # Por eso aplicamos el decorador directamente con power como
    # primer argumento explícito en la firma y lo pasamos bien.
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell with power validation."""
        # Validamos el poder manualmente aquí para respetar
        # la firma del método de instancia (self, spell_name, power).
        if power < 10:
            return "Insufficient power for this spell"
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    print("Testing spell timer...")

    @spell_timer
    def fireball_timed() -> str:
        time.sleep(0.1)   # simulamos que tarda un poco
        return "Fireball cast!"

    result = fireball_timed()
    print(f"Result: {result}")

    print("\nTesting power validator...")

    @power_validator(20)
    def thunder(power: int, target: str) -> str:
        return f"Thunder strikes {target} for {power} damage"

    print(thunder(10, "Dragon"))   # → Insufficient power (10 < 20)
    print(thunder(50, "Dragon"))   # → Thunder strikes Dragon for 50 damage

    print("\nTesting retrying spell...")
    attempt_count = [0]   # usamos lista para poder mutar desde inner scope

    @retry_spell(3)
    def unstable_spell() -> str:
        attempt_count[0] += 1
        if attempt_count[0] < 3:
            raise Exception("Spell unstable!")
        return "Waaaaaaagh spelled !"

    @retry_spell(3)
    def always_fails() -> str:
        raise Exception("Always fails")

    print(always_fails())
    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Alex"))
    print(MageGuild.validate_mage_name("X2"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
