#!/usr/bin/env python3

import sys


def ft_ancient_text() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return

    print("---")
    data = f.read()
    f.close()

    for line in data.splitlines():
        print(line)

    print("---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
