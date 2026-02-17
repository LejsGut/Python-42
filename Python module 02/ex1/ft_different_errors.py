def garden_operations(operation_type, value=None):
    plants = {"rose": 5, "tulip": 7, "daisy": 8}

    if operation_type == "parse number":
        return int(value)
    elif operation_type == "divide_harvest":
        total_harvest = 20
        return total_harvest / value
    elif operation_type == "read_file":
        with open(value, "r") as f:
            return f.read()
    elif operation_type == "access_plant":
        return plants[value]


def test_error_types():
    print("=== Garden Error Types Demo ===")

    # Test ValueError
    try:
        print("Testing ValueError...")
        garden_operations("parse number", "not_a_number")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

    # Test ZeroDivisionError
    try:
        print("Testing ZeroDivisionError...")
        garden_operations("divide_harvest", 0)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    # Test FileNotFoundError
    try:
        print("Testing FileNotFoundError...")
        garden_operations("read_file", "missing.txt")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    # Test KeyError
    try:
        print("Testing KeyError...")
        garden_operations("access_plant", "missing_plant")
    except KeyError as e:
        print(f"Caught KeyError: {e}")

    # Test multiple errors together
    try:
        print("Testing multiple errors together...")
        garden_operations("divide_harvest", 0)
        garden_operations("parse number", "not_a_number")
    except Exception as e:
        print(f"Caught an error, but program continues! {e}")

    print("All error types tested successfully!")


def main():
    test_error_types()


if __name__ == "__main__":
    main()
