class Plant:
    def __init__(self, name, starting_height, starting_age, amount_plants):
        self.name = name
        self.starting_height = starting_height
        self.starting_age = starting_age
        self.amount_plants = amount_plants

    def info(self):
        print(f"Created: {self.name} ({self.starting_height}cm, "
              f"{self.starting_age} days)")

    def how_many_created(self):
        print(f"Total plants created: {count}")


Rose = Plant("Rose", 25, 30, 5)
Oak = Plant("Oak", 200, 365, 5)
Cactus = Plant("Cactus", 5, 90, 5)
Sunflower = Plant("Sunflower", 80, 45, 5)
Fern = Plant("Fern", 15, 120, 5)

print("=== Plant Factory Output ===")
plants = [Rose, Oak, Cactus, Sunflower, Fern]
count = 0
while count < Rose.amount_plants:
    plants[count].info()
    count += 1
print("")
Rose.how_many_created()
