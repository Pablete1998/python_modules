#!/usr/bin/env python3

import sys


def ft_archive_creation() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
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

    print("Transform data:")
    print("---")
    transformed = []
    for line in data.splitlines():
        new_line = line + "#"
        transformed.append(new_line)
        print(new_line)
    print("---")

    new_name = input("Enter new file name (or empty): ")

    if new_name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_name}'")
    try:
        f2 = open(new_name, "w")
        for line in transformed:
            f2.write(line + "\n")
        f2.close()
    except Exception as e:
        print(f"Error saving file '{new_name}': {e}")
        return

    print(f"Data saved in file '{new_name}'.")
