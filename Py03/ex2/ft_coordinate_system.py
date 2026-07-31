#!/usr/bin/env python3

import math


def get_coordinates() -> tuple[float, float, float]:
    while True:
        coordset = input("Enter new coordinates as floats in format 'x,y,z': ")
        coord = coordset.split(',')
        if len(coord) != 3:
            print("Invalid syntax")
            continue
        try:
            x = float(coord[0].strip())
            y = float(coord[1].strip())
            z = float(coord[2].strip())
            return (x, y, z)
        except ValueError as e:
            for err in (coord[0].strip(), coord[1].strip(), coord[2].strip()):
                try:
                    float(err)
                except ValueError:
                    print(f"Error on parameter '{err}': {e}")
                    break
            continue


def distance_center(coord: tuple[float, float, float]) -> float:
    x, y, z = coord
    return math.sqrt(x**2 + y**2 + z**2)


def distance_sets(
    coord1: tuple[float, float, float],
    coord2: tuple[float, float, float]
) -> float:
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def main():
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    coord1 = get_coordinates()
    print(f"Got a first tuple: {coord1}")
    print(f"It includes: X={coord1[0]}, Y={coord1[1]}, Z={coord1[2]}")
    d1 = distance_center(coord1)
    print(f"Distance to center: {round(d1, 4)}")
    print()
    print("Get a second set of coordinates")
    coord2 = get_coordinates()
    d2 = distance_sets(coord1, coord2)
    print(f"Distance between the 2 sets of coordinates: {round(d2, 4)}")


if __name__ == "__main__":
    main()
