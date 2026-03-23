#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        self.height += 0.8

    def age_one_day(self):
        self.age += 1

    def show(self):
        print(f"{self.name}: {self.height}cm, {self.age} days old")


p1 = Plant("Rose", 25, 30)
p2 = Plant("Sunflower", 80, 45)
p3 = Plant("Cactus", 15, 120)

if __name__ == "__main__":
    print("=== Garden Plant Growth ===")

    plant = Plant("Rose", 25.0, 30)

    initial_height = plant.height

    for day in range(1, 8):
        plant.grow()
        plant.age_one_day()

        print(f"=== Day {day} ===")
        print(
            f"{plant.name}: {round(plant.height, 1)}cm, "
            f"{plant.age} days old"
        )

    total_growth = round(plant.height - initial_height, 1)
    print(f"Growth this week: {total_growth}cm")
