#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    x1 = (-b + math.sqrt(b*b-4*a*c))/(2*a)
    x2 = (-b - math.sqrt(b*b-4*a*c))/(2*a)

    return (x1,x2)

def main():
    a = 1
    b = 3
    c = 2
    print(solve_quadratic(a,b,c))

if __name__ == "__main__":
    main()
