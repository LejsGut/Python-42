def check_plant_health(plant_name, water_level, sunlight_hours):
    # 1) Plant name: nicht leer
    if not isinstance(plant_name, str) or plant_name.strip() == "":
        raise TypeError("Plant name must be a non-empty string.")

    # 2) Water level: 1..10
    if not isinstance(water_level, int):
        raise TypeError("Water level must be an integer.")
    if water_level < 1 or water_level > 10:
        raise ValueError("Water level must be between 1 and 10.")

    # 3) Sunlight: 2..12
    if not isinstance(sunlight_hours, int):
        raise TypeError("Sunlight hours must be an integer.")
    if sunlight_hours < 2 or sunlight_hours > 12:
        raise ValueError("Sunlight hours must be between 2 and 12.")

    return f"{plant_name} is healthy: water={water_level}, sunlight={sunlight_hours}h"


def test_plant_checks():
    print("=== Plant Health Checks ===")

    # Test valid input
    try:
        result = check_plant_health("Rose", 5, 6)
        print(result)
    except Exception as e:
        print(f"Unexpected error: {e}")

    # Test invalid plant name
    try:
        check_plant_health("", 5, 6)
    except TypeError as e:
        print(f"Caught TypeError: {e}")

    # Test invalid water level (too low)
    try:
        check_plant_health("Tulip", 0, 6)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    # Test invalid water level (too high)
    try:
        check_plant_health("Daisy", 11, 6)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    # Test invalid sunlight hours (too low)
    try:
        check_plant_health("Sunflower", 5, 1)
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    # Test invalid sunlight hours (too high)
    try:
        check_plant_health("Lily", 5, 13)
    except ValueError as e:
        print(f"Caught ValueError: {e}")


def main():
    test_plant_checks()


if __name__ == "__main__":
    main()
