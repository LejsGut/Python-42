class GardenError(Exception):
    pass

class Gardenmanager:
    water_tank = 2

    def __init__(self, name):
        self.name = name
        self.plants = list()

    def add_plants(self, plant, water_level, plant_health, sunlight_hours):
        if not isinstance(plant, str) or plant.strip() == "":
            print("Plant name cannot be empty!")
            return
        self.plants.append(
            {
                "plant": plant,
                "water_level": water_level,
                "plant_health": plant_health,
                "sunlight_hours": sunlight_hours,
            }
        )
        print(f"Plant {plant} added successfully!")

    def watering_plants(self, plants_to_water):
        print("Open watering system")
        try:
            for plant in plants_to_water:
                try:
                    if not isinstance(plant, str):
                        raise TypeError("Invalid plant type!")


                    print(f"Watering {plant}")
                    Gardenmanager.water_tank -= 1
                    if Gardenmanager.water_tank <= 0:
                        raise GardenError("Not enough water in tank")
                        Gardenmanager.water_tank += 1
                        print("System recovered and coninuing...")

                    for p in self.plants:
                        if p["plant"] == plant:
                            p["water_level"] += 1
                            break

                except TypeError:
                    print(f"Error: Cannot water {plant} - invalid plant!")
                    continue
        finally:
            print("Close watering system (cleanup)")
            print("Cleanup always happens, even if there was an error!")


    def check_plant_health(
        self, plant, water_level, plant_health, sunlight_hours
    ):
        if not isinstance(plant, str) or plant.strip() == "":
            raise TypeError("Plant name cannot be empty!")
        if (
            not isinstance(water_level, int)
            or water_level < 1
            or water_level > 10
        ):
            raise ValueError(
                "Water level must be an integer between 1 and 10."
            )
        if plant_health != "good":
            raise ValueError("Plant health must be 'good'.")
        if (
            not isinstance(sunlight_hours, int)
            or sunlight_hours < 2
            or sunlight_hours > 12
        ):
            raise ValueError(
                "Sunlight hours must be an integer between 2 and 12."
            )
        return (
            f"{plant} is healthy: water={water_level}, "
            f"sunlight={sunlight_hours}h"
        )

def test_garden_manager():
    manager = Gardenmanager("alice")
    print("Adding plants to the garden...")
    manager.add_plants("rose", 5, "good", 6)
    manager.add_plants("tulip", 3, "wilted", 4)
    manager.add_plants("daisy", 8, "good", 13)
    manager.add_plants("", 4, "good", 5)

    print("\nWatering plants...")
    manager.watering_plants(["rose", "tulip", "daisy", 123])

    print("\nChecking plant health...")
    try:
        print(manager.check_plant_health("rose", 5, "good", 6))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
    try:
        print(manager.check_plant_health("daisy", 8, "good", 13))
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    print

def main():
    test_garden_manager()

if __name__ == "__main__":    main()