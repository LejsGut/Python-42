class Plant:
    def __init__(self, name, age, height, how_many):
        self.name = name
        self.age = age
        self.height = height
        self.how_many = how_many

    def check_height(self):
        if Rose.height < 1:
            print(
                f"Invalid operation attempted: height"
                f" {Rose.height} [REJECTED]"
            )
            print("Security: Negative height rejected")
        else:
            print(f"Height updated: {Rose.height}cm [OK]")

    def check_age(self):
        if Rose.age < 1:
            print(f"Invalid operation attempted: age {Rose.age} [REJECTED]")
            print("Security: Negative age or null age rejected")
        else:
            print(f"Age updated: {Rose.age} days [OK]")

    def info(self):
        print(
            f"Current Plant: {self.name} ({self.height}cm, "
            f"{self.age} days)"
        )

    def plant_created(self):
        print(f"Plant created: {self.name}")


count = 0
Rose = Plant("Rose", -1, 1, 1)
plants = [Rose]
print("=== Garden Security System ===")
while count < Rose.how_many:
    plants[count].plant_created()
    Rose.check_height()
    Rose.check_age()
    Rose.info()
    count += 1
