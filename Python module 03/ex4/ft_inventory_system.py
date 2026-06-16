import sys


def parse_inventory() -> dict[str, int]:
    inventory: dict[str, int] = {}
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


def display_stats(inv: dict[str, int]) -> None:
    print(f"Got inventory: {inv}")
    print(f"Item list: {list(inv.keys())}")
    total = sum(inv.values())
    print(f"Total quantity of the {len(inv)} items: {total}")
    for item in inv.keys():
        print(f"Item {item} represents {round(inv[item] / total * 100, 1)}%")
    most: str | None = None
    least: str | None = None
    for item in inv.keys():
        if most is None or inv[item] > inv[most]:
            most = item
        if least is None or inv[item] < inv[least]:
            least = item
    if most is not None and least is not None:
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
