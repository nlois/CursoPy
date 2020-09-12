#!/usr/bin/env python3

def merge(L1, L2):
    L = L1 + L2
    sorted = 0
    n = len(L)
    while sorted != n-1 :
        sorted = 0
        for i in range(n-1) :
            left=L[i]
            right=L[i+1]
            if left > right:
                L[i+1] = left
                L[i] = right
            else:
                sorted = sorted + 1
    return(L)

def main():
    L1 = [1,3,5,7]
    L2 = [5,6,1,3]
    print(merge(L1,L2))

if __name__ == "__main__":
    main()
