#!/usr/bin/env python3


import math


def get_player_pos():
    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = coords.split(",")
        if len(parts) != 3 or any(p.strip() == "" for p in parts):
            print("Invalid syntax")
            continue
        try:
            x, y, z = map(float, parts)
            return (x, y, z)
        except ValueError as e:
            # Encontrar cuál parámetro falló
            for p in parts:
                try:
                    float(p)
                except ValueError:
                    print(f"Error on parameter '{p}': {e}")
                    break


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("")
    print("Get a first set of coordinates")
    tup1 = get_player_pos()
    print(f"Got a first tuple: {tup1}")
    print(f"It includes: X={tup1[0]}, Y={tup1[1]}, Z={tup1[2]}")
    dist_center = math.sqrt(tup1[0]**2 + tup1[1]**2 + tup1[2]**2)
    print(f"Distance to center: {round(dist_center, 4)}")
    print("")

    print("Get a second set of coordinates")
    tup2 = get_player_pos()
    dist_between = math.sqrt(
        (tup2[0] - tup1[0])**2 +
        (tup2[1] - tup1[1])**2 +
        (tup2[2] - tup1[2])**2
        )
    print(
        f"Distance between the 2 sets of coordinates: "
        f"{round(dist_between, 4)}"
        )
