class Plant:
    """A plant that can grow() and age() over time.

    The age value is stored in ``day`` (instead of ``age``) so the class
    can also expose an ``age()`` method: an attribute and a method may
    not share the same name on an instance.
    """

    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0.0
        self.day: int = 0
        self.growth_rate: float = 0.0

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.day += 1

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm, "
              f"{self.day} days old")


def main() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose.day = 30
    rose.growth_rate = 0.8

    start_height = rose.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.show()
        rose.grow()
        rose.age()

    print(f"Growth this week: {round(rose.height - start_height)}cm")


if __name__ == "__main__":
    main()
