import sys


def parse_inventory() -> dict:
    inventory = {}
    for arg in sys.argv[1:]:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if parts[0] in inventory:
            print(f"Redundant item '{parts[0]}' - discarding")
            continue
        try:
            inventory[parts[0]] = int(parts[1])
        except ValueError as e:
            print(f"Quantity error for '{parts[0]}': {e}")
            continue
    return inventory


def display_stats(inv: dict) -> None:
    print(f"Got inventory: {inv}")
    print(f"Item list: {list(inv.keys())}")
    total = sum(inv.values())
    print(f"Total quantity of the {len(inv)} items: {total}")
    for item, quantity in inv.items():
        print(f"Item {item} represents {round(quantity / total * 100, 1)}%")
    most = None
    least = None
    for item, quantity in inv.items():
        if most is None or quantity > inv[most]:
            most = item
        if least is None or quantity < inv[least]:
            least = item
    print(f"Item most abundant: {most} with quantity {inv[most]}")
    print(f"Item least abundant: {least} with quantity {inv[least]}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inv = parse_inventory()
    display_stats(inv)
    inv.update({"magic_item": 1})
    print(f"Updated inventory: {inv}")


if __name__ == "__main__":
    main()
