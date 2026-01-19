class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def info(self):
        print(
            f"{self.name} ({self.__class__.__name__}): "
            "f{self.height}cm, {self.age} days, ",
            end="",
        )


class Flower(Plant):

    def __init__(self, name, height, age, colour):
        super().__init__(name, height, age)
        self.colour = colour

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def info(self):
        super().info()
        print(f"{self.colour}")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def info(self):
        super().info()
        print(f"{self.harvest_season}")
        print(f"{self.name} {self.nutritional_value}")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter, shade):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade = shade

    def info(self):
        super().info()
        print(f"{self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.shade} square " "fmeters of shade")


def main() -> None:
    Rose = Flower("Rose", 25, 30, "red colour")
    Tulip = Flower("Tulip", 30, 35, "yellow colour")

    Tomato = Vegetable("Tomato", 80, 90, "summer harvest", "has salt")
    Cucumber = Vegetable("Cucumber", 60, 85, "summer harvest", "has no salt")

    Oak = Tree("Oak", 500, 1825, 50, 5)
    Pine = Tree("Pine", 300, 1200, 40, 5)

    print("=== Garden Plant Types ===")
    plants = [Tomato, Cucumber, Rose, Tulip, Oak, Pine]
    for plant in plants:
        plant.info()
        print()


if __name__ == "__main__":
    main()
