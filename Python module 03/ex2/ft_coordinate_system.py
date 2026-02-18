import sys
import math

def main(argv: list[str]) -> None:
    print("=== Game Coordinate System ===")

    position_created = (10, 20, 5)
    x1, y1, z1 = position_created
    start_position = (0, 0, 0)
    x2, y2, z2 = start_position
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
    distance_rounded = round(distance, 2)
    print(f"Position created: {position_created}")
    print(f"Distand between {start_position} and {position_created}: {distance_rounded}")
    
    position_text = "3,4,0"
    false_position_text = "abc,def,ghi"
    parts = position_text.split(",")
    parts2 = false_position_text.split(",")
    try:
        x3 = int(parts[0])
        y3 = int(parts[1])
        z3 = int(parts[2])
        parsed_position = (x3, y3, z3)
    except ValueError:
        print("Is not a valid number")
        return
    else:
        distance = math.sqrt((x3 - x2)**2 + (y3 - y2)**2 + (z3 - z2)**2)
        print(f"{distance} is the distance from {parsed_position} to {start_position}")

    try:
        x4 = int(parts2[0])
        y4 = int(parts2[1])
        z4 = int(parts2[2])
        parsed_position = (x4, y4, z4)
    except ValueError:
        print("Is not a valid number")
        return
    else:
        distance = math.sqrt((x4 - x2)**2 + (y4 - y2)**2 + (z4 - z2)**2)

    teleport_position = (3, 4, 0)

    x, y, z = teleport_position

    print(f"Teleport unpacking: x={x}, y={y}, z={z}")

if __name__ == "__main__":
    main(sys.argv)