def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        number = int("abc")
        print(number)
    elif operation_number == 1:
        result = 5 / 0
        print(result)
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        text = "abc"
        number = 123
        print(text + number)  # type: ignore[operator]
    else:
        print("Operation completed successfully")


def test_error_types(operation_number: int) -> None:
    try:
        garden_operations(operation_number)
    except ValueError as error:
        print(f"Caught ValueError: {error}")
    except ZeroDivisionError as error:
        print(f"Caught ZeroDivisionError: {error}")
    except FileNotFoundError as error:
        print(f"Caught FileNotFoundError: {error}")
    except TypeError as error:
        print(f"Caught TypeError: {error}")


def main() -> None:
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    test_error_types(0)
    print("Testing operation 1...")
    test_error_types(1)
    print("Testing operation 2...")
    test_error_types(2)
    print("Testing operation 3...")
    test_error_types(3)
    print("Testing operation 4...")
    test_error_types(4)
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
