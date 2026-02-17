def water_plants(plant_list):
    print("Open watering system")
    try:
        for plant in plant_list:
            if isinstance(plant, str):
                print(f"Watering {plant}")
            else:
                raise TypeError
    except Exception as e:
        print(f"Error: Cannot water {e} - invalid plant!")
    finally:
        print("Close watering system (cleanup)")
    print("Cleanup always happens, even if there was an error!")


def test_watering_system():
    allowed_list = ["rose", "tulip", "daisy"]
    water_plants(allowed_list)
    bad_list = ["rose", "tulip", None, "daisy"]
    water_plants(bad_list)


def main():
    test_watering_system()


if __name__ == "__main__":
    main()
