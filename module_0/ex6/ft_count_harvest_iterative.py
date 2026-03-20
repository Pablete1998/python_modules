#!/usr/bin/env python3

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    min = 1
    while (min <= days):
        print(f"Day {min}")
        min = min + 1
    print("Harvest time!")
