#!/usr/bin/env python3

def nice_sort(L):
    n = len(L)
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

def detect_ranges(L1):
    L=sorted(L1)
    n = len(L)
    Lista = []

    t1=0
    t2=0

    i=0
    j=0

    LA = []
    LD = []


    while i < n-1:
        if L[i+1] - L[i] > 1:
            LA.append(False)
        else:
            LA.append(True)
        i=i+1
    if L[n-1] == L[n-2]+1:
        LA.append(True)
    else:
        LA.append(False)

    i=n-1
    while i > 0:
        if L[i] - L[i-1] == 1:
            LD.insert(0,True)
        else:
            LD.insert(0,False)
        i=i-1
    if L[0] == L[1]+1:
        LD.insert(0,True)
    else:
        LD.insert(0,False)

    for i in range(len(LA)-1):
        if LA[i] == False and LD [i] == False:
            Lista.append(L[i])

        elif LA[i] == True and LD [i] == False:
            t1=L[i]
        elif LA[i] == False and LD [i] == True:
            t2=L[i]+1
            t = (t1,t2)

            Lista.append(t)
    if LA[n-1] == True and LD[n-1] == True:
        t2=L[n-1]
        t= (t1,t2+1)
        Lista.append(t)
    else:
        Lista.append(L[n-1])

    return(Lista)

def main():
    L = [-4, -2, 0, 2, 4]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()






    # while L[i+1] == L[i]+1:
    #     if j==0:
    #         t1=L[i]
    #         print(i,j,t1)
    #         j=j+1
    #     else :
    #         t2=L[i]
    #         print("tupla fin")
    #         print(t2)
    #         t = (t1,t2)
    #         Lista.append(t)
    #         j=0
    #         i=i+1
    #         Lista.append(L[i])
