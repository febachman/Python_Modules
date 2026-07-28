#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="A general garden error occurred."):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def check_plant_health(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_plant_watering(water_level: int) -> None:
    if water_level <= 0:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("Testing PlantError...")
    try:
        check_plant_health(is_wilting=True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()
    print("Testing WaterError...")
    try:
        check_plant_watering(water_level=0)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()
    print("Testing catching all garden errors...")
    errors_to_test = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ]
    for err in errors_to_test:
        try:
            raise err
        except GardenError as e:
            print(f"Caught GardenError: {e}")
    print()
    print("All custom error types work correctly!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    test_custom_errors()


if __name__ == "__main__":
    main()
