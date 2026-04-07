#!/usr/bin/env python3

import sys


def ft_stream_management() -> None:
    # 1. Comprobar argumentos
    if len(sys.argv) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    # 2. Intentar abrir archivo original
    try:
        f = open(filename, "r")
    except Exception as e:
        print(
            f"[STDERR] Error opening file '{filename}':"
            f" {e}", file=sys.stderr
            )
        return

    print("---")
    data = f.read()
    f.close()

    # 3. Mostrar contenido original
    for line in data.splitlines():
        print(line)
    print("---")
    print(f"File '{filename}' closed.")

    # 4. Transformar datos
    print("Transform data:")
    print("---")
    transformed = []
    for line in data.splitlines():
        new_line = line + "#"
        transformed.append(new_line)
        print(new_line)
    print("---")

    # 5. Leer nombre de archivo SIN input()
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_name = sys.stdin.readline().rstrip("\n")

    if new_name == "":
        print("Not saving data.")
        return

    # 6. Guardar archivo nuevo
    print(f"Saving data to '{new_name}'")
    try:
        f2 = open(new_name, "w")
        for line in transformed:
            f2.write(line + "\n")
        f2.close()
    except Exception as e:
        print(
            f"[STDERR] Error opening file '{new_name}':"
            f" {e}", file=sys.stderr)
        print("Data not saved.")
        return

    print(f"Data saved in file '{new_name}'.")


if __name__ == "__main__":
    ft_stream_management()
