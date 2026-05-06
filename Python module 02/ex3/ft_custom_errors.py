class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def is_plant_healthy(plant: str, is_healthy: bool) -> None:
    if is_healthy:
        print(f"{plant} is healthy")
    else:
        raise PlantError(f"The {plant} plant is wilting!")


def is_it_enough_water(has_enough_water: bool) -> None:
    if has_enough_water:
        print("There is enough water")
    else:
        raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    try:
        is_plant_healthy("tomato", False)
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print()

    print("Testing WaterError...")
    try:
        is_it_enough_water(False)
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print()

    print("Testing catching all garden errors...")
    try:
        is_plant_healthy("tomato", False)
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    try:
        is_it_enough_water(False)
    except GardenError as error:
        print(f"Caught GardenError: {error}")

    print()
    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()