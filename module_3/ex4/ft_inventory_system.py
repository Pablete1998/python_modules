#!/usr/bin/env python3


import sys


def parse_inventory():
    args = sys.argv[1:]
    inventory = {}
    seen = set()

    for param in args:
        if ":" not in param:
            print(f"Error - invalid parameter '{param}'")
            continue

        item, qty = param.split(":", 1)

        if item in seen:
            print(f"Redundant item '{item}' - discarding")
            continue

        seen.add(item)

        try:
            quantity = int(qty)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

        inventory[item] = quantity

    return inventory


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inventory = parse_inventory()

    if len(inventory) == 0:
        print(
            "At the beginning of the game, "
            "your inventory is usually empty ;)"
            )
        sys.exit(0)

    print(f"Got inventory: {inventory}")

    # Item list
    items = list(inventory.keys())
    print(f"Item list: {items}")

    # Total quantity
    total_qty = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total_qty}")

    # Percentages
    for item, qty in inventory.items():
        percent = round((qty / total_qty) * 100, 1)
        print(f"Item {item} represents {percent}%")

    # Most abundant (respecting order)
    most_item = None
    least_item = None
    for item in items:
        if most_item is None or inventory[item] > inventory[most_item]:
            most_item = item
        if least_item is None or inventory[item] < inventory[least_item]:
            least_item = item

    print(
        f"Item most abundant: {most_item}"
        f" with quantity {inventory[most_item]}"
        )
    print(
        f"Item least abundant: {least_item} "
        f"with quantity {inventory[least_item]}"
        )

    # Add new item
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
