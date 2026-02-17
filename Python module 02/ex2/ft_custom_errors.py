class GardenError(Exception):
    """Base class for garden-related errors"""

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    """Error related to plant issues"""

    def __init__(self, message):
        super().__init__(message)


class WaterError(GardenError):
    """Error related to watering issues"""

    def __init__(self, message):
        super().__init__(message)


def check_plant_health(plant, health):
    if health != "good":
        raise PlantError(f"Plant '{plant}' is wilting!")


def check_watering(water):
    if water < 1:
        raise WaterError("Not enough water for the garden!")
    elif water > 10:
        raise WaterError("Too much water! Risk of root rot!")


def test_custom_errors():
    print("=== Garden Custom Errors Demo ===\n")  # <- neue Zeile lohnt sich

    # Test PlantError
    try:
        print("Testing PlantError...")
        check_plant_health("Rose", "wilting")
    except PlantError as e:
        print(f"Caught PlantError: {e.message}")

    # Test WaterError for too little water
    try:
        print("Testing WaterError for too little water...")
        check_watering(0)
    except WaterError as e:
        print(f"Caught WaterError: {e.message}")

    # Test WaterError for too much water
    try:
        print("Testing WaterError for too much water...")
        check_watering(15)
    except WaterError as e:
        print(f"Caught WaterError: {e.message}")

    print(
        "\nTesting catching all errors with base class..."
    )  # <- neue Zeile lohnt sich

    print("Testing watering error...")
    try:
        check_watering(0)
    except GardenError as e:
        print(f"Caught GardenError: {e.message}")

    print()  # <- neue Leerzeile lohnt sich hier (trennt die beiden Base-Tests)

    print("Testing plant health error...")
    try:
        check_plant_health("Tulip", "wilted")
    except GardenError as e:
        print(f"Caught GardenError: {e.message}")

    print("\nAll custom error tests completed successfully!")


def main():
    test_custom_errors()


if __name__ == "__main__":
    main()
