#!/usr/bin/env python3

def ft_count_harvest_recursive():
    def count(day, total):
        if day > total:
            return
        print(f"Day {day}")
        count(day + 1, total)
    days = int(input("Days until harvest: "))
    count(1, days)
    print("Harvest time!")
