#!/usr/bin/env python3
"""
FuncMage Chronicles - Exercise 0: Lambda Sanctum
Master the art of anonymous functions and lambda expressions.
"""
from typing import TypedDict


class Artifact(TypedDict):
    name: str
    power: int
    type: str


class Mage(TypedDict):
    name: str
    power: int
    element: str


def artifact_sorter(artifacts: list[Artifact]) -> list[Artifact]:
    """Sort magical artifacts by power level in descending order."""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[Mage], min_power: int) -> list[Mage]:
    """Filter mages whose power level meets the minimum threshold."""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """Transform spell names by adding mystical prefix and suffix."""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[Mage]) -> dict[str, int | float]:
    """Calculate power statistics across all mages."""
    max_power = max(mages, key=lambda m: m['power'])['power']
    min_power = min(mages, key=lambda m: m['power'])['power']
    avg_power = round(sum(map(lambda m: m['power'], mages)) / len(mages), 2)
    return {'max_power': max_power, 'min_power': min_power,
            'avg_power': avg_power}


if __name__ == "__main__":
    artifacts: list[Artifact] = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'focus'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'weapon'},
        {'name': 'Shadow Blade', 'power': 78, 'type': 'weapon'},
        {'name': 'Storm Crown', 'power': 110, 'type': 'relic'},
    ]
    mages: list[Mage] = [
        {'name': 'Alex', 'power': 73, 'element': 'fire'},
        {'name': 'Jordan', 'power': 95, 'element': 'lightning'},
        {'name': 'Riley', 'power': 60, 'element': 'ice'},
        {'name': 'Sage', 'power': 88, 'element': 'wind'},
        {'name': 'Nova', 'power': 50, 'element': 'shadow'},
    ]
    spells = ['fireball', 'heal', 'shield']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        f" comes before {sorted_artifacts[1]['name']}"
        f" ({sorted_artifacts[1]['power']} power)"
    )
    print("\nTesting power filter...")
    powerful = power_filter(mages, 80)
    print(f"Mages with power >= 80: {[m['name'] for m in powerful]}")
    print("\nTesting spell transformer...")
    print(*spell_transformer(spells))
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max: {stats['max_power']} | Min: {stats['min_power']}"
          f" | Avg: {stats['avg_power']}")
