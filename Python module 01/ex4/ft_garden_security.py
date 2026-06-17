class Plant:
    """A plant that protects its data through encapsulation.

    Height and age are kept in "protected" attributes (single leading
    underscore convention, not name mangling) and can only be modified
    through validated setters.
    """

    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self._height: float = float(height) if height >= 0 else 0.0
        self._age: int = age if age >= 0 else 0

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> bool:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
            return False
        self._height = float(height)
        print(f"Height updated: {height}cm")
        return True

    def set_age(self, age: int) -> bool:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
            return False
        self._age = age
        print(f"Age updated: {age} days")
        return True

    def show(self) -> None:
        print(f"{self.name}: {round(self._height, 1)}cm, "
              f"{self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25)
    rose.set_age(30)
    print()

    if not rose.set_height(-5):
        print("Height update rejected")
    if not rose.set_age(-3):
        print("Age update rejected")
    print()

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
