class Plant:
    """Common features plus a nested statistics tracker."""

    class _Stats:
        """Encapsulated statistics for a single plant."""

        def __init__(self) -> None:
            self._grow_calls = 0
            self._age_calls = 0
            self._show_calls = 0

        def record_grow(self) -> None:
            self._grow_calls += 1

        def record_age(self) -> None:
            self._age_calls += 1

        def record_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_calls} grow, "
                  f"{self._age_calls} age, {self._show_calls} show")

    def __init__(self, name: str, height: float, age: int,
                 growth_rate: float = 1.0) -> None:
        self.name = name
        self._height: float = float(height) if height >= 0 else 0.0
        self._age: int = age if age >= 0 else 0
        self._growth_rate = growth_rate
        self._stats = self._create_stats()

    def _create_stats(self) -> "Plant._Stats":
        return Plant._Stats()

    @staticmethod
    def is_older_than_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0, 0)

    def grow(self) -> None:
        self._stats.record_grow()
        self._height += self._growth_rate

    def age(self, days: int = 1) -> None:
        self._stats.record_age()
        self._age += days

    def show(self) -> None:
        self._stats.record_show()
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")

    def display_stats(self) -> None:
        self._stats.display()


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
    """A plant that can produce_shade() and tracks the shade calls."""

    class _Stats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_calls = 0

        def record_shade(self) -> None:
            self._shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_calls} shade")

    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = float(trunk_diameter)

    def _create_stats(self) -> "Tree._Stats":
        return Tree._Stats()

    def produce_shade(self) -> None:
        stats = self._stats
        if isinstance(stats, Tree._Stats):
            stats.record_shade()
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

    def age(self, days: int = 1) -> None:
        super().age(days)
        self._nutritional_value += 0.5 * days

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {round(self._nutritional_value)}")


class Seed(Flower):
    """A flower that holds its seed count once it has bloomed."""

    def __init__(self, name: str, height: float, age: int,
                 color: str, growth_rate: float = 1.0) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self._seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")


def display_statistics(plant: Plant) -> None:
    """Display statistics for any kind of plant."""
    print(f"[statistics for {plant.name}]")
    plant.display_stats()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print()

    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red", growth_rate=8.0)
    rose.show()
    display_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)
    print()

    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_statistics(oak)
    print()

    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, "yellow", growth_rate=30.0)
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)
    print()

    print("=== Anonymous")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    main()
