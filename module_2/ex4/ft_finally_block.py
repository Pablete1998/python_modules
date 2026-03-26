#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="General garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


def water_plant(plant_name):
    if plant_name.capitalize() != plant_name:
        raise PlantError(f"invalid plant name to water: '{plant_name}'")
    else:
        print(f"Watering {plant_name}: [OK]")


def test_Watering_system(plants):
    print("Opening watering system")
    try:
        for plant in plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
        print(".. ending tests and returning to main")
        return
    finally:
        print("Closing watering system")


if __name__ == "__main__":
    print("=== Garden Watering System ===")
    print("")
    print("Testing valid plants...")
    valid_plants = ["Tomato", "Lettuce", "Carrots"]
    test_Watering_system(valid_plants)
    invalid_plants = ["Tomato", "lettuce", "carrots"]
    print("")
    print("Testing invalid plants...")
    test_Watering_system(invalid_plants)
    print("")
    print("Cleanup always happens, even with errors!")
