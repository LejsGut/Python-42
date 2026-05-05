class TempError(Exception):
    pass

def input_temperature(temp_str):
    temp = int(temp_str)
    if temp > -1 and temp < 41:
        return temp
    if temp > 40:
        raise TempError(f"Caught input_temperature error: {temp_str} is too hot for plants (max 40°C) ")
    if temp < 0:
        raise TempError(f"Caught input_temperature error: {temp_str} is too cold for plants (min 0°C)")

def test_temperature(temp_str):
    print(f"Input data is '{temp_str}'")
    try:
        temp = input_temperature(temp_str)
        print(f"Temperature is now {temp}\u00B0C")
    except ValueError:
        print(f"Caught input_temperature error: invalid literal for int() with base 10: '{temp_str}'")
    except TypeError:
        print(f"{temp_str} is the wrong datatype")
    except TempError as error:
        print(error)


def main():
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature("25")
    print()
    test_temperature("abc")
    print()
    test_temperature("100")
    print()
    test_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")

if __name__ == "__main__":
    main()
