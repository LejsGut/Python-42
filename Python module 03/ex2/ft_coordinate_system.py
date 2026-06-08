import sys
import math

def get_player_pos():
    while True:
        pos = input("Enter new coordinates as floats in format 'x,y,z': ")
        coordinates = pos.split(",")
        if len(coordinates) != 3:
            print("Invalid syntax")
            continue
        valid = True
        floats = []
        for part in coordinates:
            try:
                floats.append(float(part.strip()))
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
                valid = False
                break
        if not valid:
            continue
        coordinates = (floats[0], floats[1], floats[2])
        return coordinates

def print_coordinates(coordinates):
    x, y, z = coordinates
    print(f"It includes: x={x}, y={y}, z={z}")

def distance_from_origin(coordinates):
    x, y, z = coordinates
    distance_from_origin = math.sqrt(x**2 + y**2 + z**2)
    print(f"Distance from origin: {distance_from_origin:.2f}")

def print_distance_between_points(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    distance_between_points = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between points: {distance_between_points:.2f}")

def main():
    print("=== Game Coordinate System ===")
    player_pos = get_player_pos()
    print_coordinates(player_pos)
    distance_from_origin(player_pos)


    print("get a second set of coordinates")
    second_pos = get_player_pos()
    print_distance_between_points(player_pos, second_pos)

if __name__ == "__main__":
    main()