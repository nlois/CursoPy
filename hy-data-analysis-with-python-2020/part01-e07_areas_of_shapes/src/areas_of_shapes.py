#!/usr/bin/env python3

import math


def main():
    # enter you solution here
    cond = True
    while cond:
        shape=input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            base = float(input("Give base of the triangle: "))
            altura = float(input("Give height of the triangle: "))
            area = base*altura/2
            print(f"The area is {area}")
        elif shape == "rectangle":
            base = float(input("Give width of the rectangle: "))
            altura = float(input("Give height of the rectangle: "))
            area = base*altura
            print(f"The area is {area}")
        elif shape == "circle":
            radio = float(input("Give radius of the circle: "))
            area = math.pi * radio**2
            print(f"The area is {area}")
        elif shape == "":
            cond = False
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
