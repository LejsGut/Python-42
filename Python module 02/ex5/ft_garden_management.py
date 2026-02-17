class Gardenmanager:
    def __init__(self, name):
        self.name = name
        self.plants = list()

    def add_plants(self, plant, water_level, plant_health, sunlight_hours):
        self.plants.append(
            {
                "plant": plant,
                "water_level": water_level,
                "plant_health": plant_health,
                "sunlight_hours": sunlight_hours,
            }
        )
        print(f"Added {plant} successfully")

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

    def watering_plants(list):
        print("Open watering system")
        try:
            for plant in list:
                if isinstance(plant, str):
                    print(f"Watering {plant}")
                    list.plant.water_level += 1
                else:
                    raise TypeError("Invalid plant type!")
        except Exception as e:
            print(f"Error: Cannot water {e} - invalid plant!")
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
