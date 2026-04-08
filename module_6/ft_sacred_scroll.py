# ft_sacred_scroll.py

import alchemy
import alchemy.elements


def safe_call(func, label: str) -> None:
    """Call a function and catch AttributeError,
    printing the correct message."""
    try:
        result = func()
        print(f"{label}: {result}")
    except AttributeError:
        print(f"{label}: AttributeError - not exposed")


def main() -> None:
    print("=== Sacred Scroll Mastery ===")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(
        "alchemy.elements.create_water(): "
        f"{alchemy.elements.create_water()}")
    print(
        f"alchemy.elements.create_earth():"
        f"{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("Testing package-level access (controlled by __init__.py):")
    safe_call(alchemy.create_fire, "alchemy.create_fire()")
    safe_call(alchemy.create_water, "alchemy.create_water()")

    # These should fail
    safe_call(lambda: alchemy.create_earth(), "alchemy.create_earth()")
    safe_call(lambda: alchemy.create_air(), "alchemy.create_air()")

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
