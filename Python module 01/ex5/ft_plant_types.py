class Plant:
    """Common features shared by every kind of plant."""

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self.name = name
        self._height: float = float(height) if height >= 0 else 0.0
        self._age: int = age if age >= 0 else 0
        self._growth_rate = growth_rate

    def grow(self) -> None:
        self._height += self._growth_rate

    def age(self) -> None:
        self._age += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")


class Flower(Plant):
    """A plant with a color that can bloom()."""

    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    """A plant with a trunk diameter that can produce_shade()."""

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = float(trunk_diameter)

    def produce_shade(self) -> None:
        print(f"Tree {self.name} now produces a shade of "
              f"{round(self._height, 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.trunk_diameter, 1)}cm")


class Vegetable(Plant):
    """A plant whose nutritional value rises as it grows and ages."""

    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self._nutritional_value: float = 0.0

    def grow(self) -> None:
        super().grow()
        self._nutritional_value += 0.5

    def age(self) -> None:
        super().age()
        self._nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {round(self._nutritional_value)}")


def main() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print()

    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", growth_rate=2.1)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age()
    tomato.show()


if __name__ == "__main__":
    main()
