#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name

        # Validación de altura
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            self._height = 0
        else:
            self._height = height

        # Validación de edad
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    # Métodos de acceso
    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    # Métodos de modificación
    def set_height(self, new_height):
        if new_height < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = new_height
            print(f"Height updated: {new_height}cm")

    def set_age(self, new_age):
        if new_age < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = new_age
            print(f"Age updated: {new_age} days")

    def show(self):
        print(f"{self.name}: {self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    plant = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    plant.show()

    plant.set_height(25)
    plant.set_age(30)

    plant.set_height(-5)
    plant.set_age(-10)

    print("Current state:", end=" ")
    plant.show()
