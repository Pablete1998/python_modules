#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="General garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def raise_plant_error():
    raise PlantError("The tomato plant is wilting!")


def raise_water_error():
    raise WaterError("Not enough water in the tank!")


def test_plant_error():
    print("Testing PlantError...")
    try:
        raise_plant_error()
    except PlantError as e:
        print("Caught PlantError:", e)


def test_water_error():
    print("Testing WaterError...")
    try:
        raise_water_error()
    except WaterError as e:
        print("Caught WaterError:", e)


def test_garden_error():
    print("Testing catching all garden errors...")
    try:
        raise_plant_error()
    except GardenError as e:
        print("Caught GardenError:", e)

    try:
        raise_water_error()
    except GardenError as e:
        print("Caught GardenError:", e)


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")

    test_plant_error()
    test_water_error()
    test_garden_error()

    print("All custom error types work correctly!")
