import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        pos = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            a, b, c = pos.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        valid = True
        floats = []
        for part in (a, b, c):
            try:
                floats.append(float(part.strip()))
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
                valid = False
                break
        if not valid:
            continue
        return (floats[0], floats[1], floats[2])


def print_coordinates(coordinates: tuple[float, float, float]) -> None:
    x, y, z = coordinates
    print(f"It includes: X={x}, Y={y}, Z={z}")


def distance_to_center(coordinates: tuple[float, float, float]) -> None:
    x, y, z = coordinates
    distance = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance to center: {distance:.4f}")


def print_distance_between_points(
    pos1: tuple[float, float, float],
    pos2: tuple[float, float, float],
) -> None:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between the 2 sets of coordinates: {distance:.4f}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    player_pos = get_player_pos()
    print(f"Got a first tuple: {player_pos}")
    print_coordinates(player_pos)
    distance_to_center(player_pos)

    print("Get a second set of coordinates")
    second_pos = get_player_pos()
    print_distance_between_points(player_pos, second_pos)


if __name__ == "__main__":
    main()
