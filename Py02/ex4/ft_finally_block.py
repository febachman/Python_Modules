#!/usr/bin/env python3

class PlantError(Exception):
    def _init_(self, plant_name):
        super()._init_(f"Invalid plant name to water: '{plant_name}'")


def water_plant(plant_name):
    if plant_name != plant_name.capitalize():
        raise PlantError(plant_name)
    print(f"Watering {plant_name}: [OK]")


def test_watering_system(plants):
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


def main():
    print("=== Garden Watering System ===")
    p1 = str(input("Enter plant 01: "))
    p2 = str(input("Enter plant 02: "))
    p3 = str(input("Enter plant 03: "))
    print()
    print("Testing valid plants...")
    test_watering_system([p1.capitalize(), p2.capitalize(), p3.capitalize()])
    print()
    print("Testing invalid plants...")
    test_watering_system([p1, p2, p3])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
