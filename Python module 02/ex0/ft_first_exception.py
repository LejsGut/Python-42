def check_temperature(temp_str):
    """checks if temperature is a numer and if its in range"""
    print(f"Start test with {temp_str}")
    try:
        temp = int(temp_str)
    except (ValueError, TypeError):
        print(f"Error: '{temp_str}' is not a valid number")
        return 0
    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return 0
    elif temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return 0
    elif temp >= 0 and temp <= 40:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp


def test_temparatur_input():
    print("=== Garden Temperature Checker ===")
    check_temperature(25)
    check_temperature("abc")
    check_temperature(100)
    check_temperature(-50)
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temparatur_input()
