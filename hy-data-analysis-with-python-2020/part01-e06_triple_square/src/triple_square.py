#!/usr/bin/env python3


def triple(x):
    return(x*3)

def square(x):
    return(x**2)

def main():
    for i in [1,2,3,4,5,6,7,8,9,10]:
        a=triple(i)
        b=square(i)
        if a >= b:
            print(f"triple({i})=={a} square({i})=={b}")
        else:
            break

if __name__ == "__main__":
    main()
