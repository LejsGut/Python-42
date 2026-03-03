import  sys
import math

def main(argv: list[str]) -> None:
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}

    for token in argv[1:]:
        if ":" not in token:
            print(f"Skipping invalid token (missing ':'): {token}")
            continue

        item, amount_str = token.split(":")

        if not item:
            print(f"Skipping invalid token (empty item name): {token}")
            continue

        try:
            amount = int(amount_str)
        except ValueError:
            print(f"Skipping invalid amount (not an int): {token}")
            continue

        if amount < 0:
            print(f"Skipping invalid amount (negative): {token}")
            continue

        inventory[item] = inventory.get(item, 0) + amount

    
    total_items = sum(inventory.values())
    unique_types = len(inventory)

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")
    print()

    
    print("=== Current Inventory ===")
    if unique_types == 0:
        print("(empty)")
    else:
        for item, amount in inventory.items():
            if total_items == 0:
                pct = 0.0
            else:
                pct = (amount / total_items) * 100.0
            print(f"{item}: {amount} units ({pct:.1f}%)")
    print()
    print("=== Inventory Statistics ===")
    max_item = ""
    max_value = 0

    for item, value in inventory.items():
        if value > max_value:
            max_value = value
            max_item = item
    print(f"Most abundant: {max_item} ({max_value} units)")
    min_item = None
    min_value = None

    for item, value in inventory.items():
        if min_value is None or value < min_value:
            min_value = value
            min_item = item
    print(f"Most abundant: {min_item} ({min_value} units)")
    print()
    print("=== Item Catagories ===")

    moderate = dict()
    scarce = dict()
    for item, value in inventory.items():
        if value > 4:
            moderate.update({item: value})
        else:
            scarce.update({item: value})
    
    print(f"Moderate {moderate}")
    print(f"Scarce {scarce}")
    print()
    print("=== Management Suggestions ===")
    restock = dict()
    for item, amount in scarce.items():
        if amount < 2:
            restock.update({item: amount})
    print("Restock needed:", end=" ")
    for item in restock.keys():
        print(item, end=", ")
    print()
    print()
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", end=" ")
    for item in inventory.keys():
        print(f"{item}", end=", ")
    print()
    print("Directory values", end=" ")
    for value in inventory.values():
        print(f"{value}", end=", ")
    print()
    print("Sample lookup - 'sword' in inventory:", "sword" in inventory)
if __name__ == "__main__":
    main(sys.argv)