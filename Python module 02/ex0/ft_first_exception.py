def input_temperature(temp_str):
    temp = int(temp_str)
    return temp

def test_temperature(temp_str):
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}\u00B0C")
    except ValueError:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{temp_str}'")
    pass

def main():
    print("=== Garden Temperature ===")
    print()
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
