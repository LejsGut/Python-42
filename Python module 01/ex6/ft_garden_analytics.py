class Gardenmanager:
    def __init__(self, gardener):
        self.gardener = gardener

    def calculate_score(self):
        score = self.height
        if self.bloom:
            score += 50
        score += self.prize * 10
        return score

    def grow(self):
        growth = self.increase
        self.height += growth
        return growth

    def validate_height(self):
        if self.height < 0:
            return False
        return True


class Node:
    def __init__(
        self, gardener, name, manager, bloom, prize, height, increase
    ):
        self.gardener = gardener
        self.name = name
        self.manager = manager
        self.bloom = bloom
        self.prize = prize
        self.height = height
        self.increase = increase
        self.next = None


# Nodes (Pflanzen)
node1 = Node("Alice", "Oak Tree", Gardenmanager("Alice"), False, 0, 1, 1)
node2 = Node("Alice", "Rose", Gardenmanager("Alice"), True, 0, 1, 1)
node3 = Node("Alice", "Sunflower", Gardenmanager("Alice"), True, 10, 1, 1)
node4 = Node("Bob", "Pine Tree", Gardenmanager("Bob"), False, 0, 1, 1)
node5 = Node("Bob", "Daisy", Gardenmanager("Bob"), True, 0, 1, 1)
node6 = Node("Bob", "Tulip", Gardenmanager("Bob"), True, 5, 1, 1)

# Linked List
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6


print("=== Garden Management System Demo ===\n")

# Pflanzen hinzufügen
current = node1
while current is not None:
    print(f"Added {current.name} to {current.gardener}'s garden")
    current = current.next

print("\nAlice is helping all plants grow...")

# Wachstum
current = node1
while current is not None and current.gardener == "Alice":
    growth = Gardenmanager.grow(current)
    print(f"{current.name} grew {growth}cm (now {current.height}cm)")
    current = current.next

print("\n=== Alice's Garden Report ===")
print("Plants in garden:")

current = node1
total_plants = 0
total_growth = 0
regular_count = 0
flowering_count = 0
prize_count = 0

while current is not None and current.gardener == "Alice":
    total_plants += 1
    total_growth += current.increase

    if current.bloom and current.prize > 0:
        prize_count += 1
        print(
            f"- {current.name}: {current.height}cm, yellow flowers (blooming), "
            f"Prize points: {current.prize}"
        )
    elif current.bloom:
        flowering_count += 1
        print(f"- {current.name}: {current.height}cm, red flowers (blooming)")
    else:
        regular_count += 1
        print(f"- {current.name}: {current.height}cm")

    current = current.next

print(f"\nPlants added: {total_plants}, Total growth: {total_growth}cm")
print(
    f"Plant types: {regular_count} regular, "
    f"{flowering_count} flowering, {prize_count} prize flowers"
)
# Gartenbewertung
current = node1
height_valid = True
while current is not None and current.gardener == "Alice":
    if not Gardenmanager.validate_height(current):
        height_valid = False
        break
    current = current.next
print(f"Height validation test: {height_valid}")


# print(
#     f"\nGarden scores - Alice: {Gardenmanager.calculate_score(Node.)},"
#     f" Bob: {Gardenmanager.calculate_score()}"
# )

# CodeCultivation Object-Oriented Garden Systems
# Example:
# $> python3 ft_garden_analytics.py
# === Garden Management System Demo ===
# Added Oak Tree to Alice's garden
# Added Rose to Alice's garden
# Added Sunflower to Alice's garden
# Alice is helping all plants grow...
# Oak Tree grew 1cm
# Rose grew 1cm
# Sunflower grew 1cm
# === Alice's Garden Report ===
# Plants in garden:
# - Oak Tree: 101cm
# - Rose: 26cm, red flowers (blooming)
# - Sunflower: 51cm, yellow flowers (blooming), Prize points: 10
# Plants added: 3, Total growth: 3cm
# Plant types: 1 regular, 1 flowering, 1 prize flowers
# Height validation test: True
# Garden scores - Alice: 218, Bob: 92
# Total gardens managed: 2
