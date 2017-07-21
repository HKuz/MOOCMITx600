#!/usr/bin/python

def main():
    L1 = []
    # print(search(L1, 1))
    # print(newsearch(L1, 1))

    L2 = [0, 1, 2, 3, 4, 5]
    # print(search(L2, 4))
    # print(newsearch(L2, 4))

    La = [2, 7, 4, 9, 11, 8, 1, 0, 16]
    # swapSort(La)
    modSwapSort(La)
    Lb = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    # swapSort(Lb)

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

def swapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)

def modSwapSort(L):
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print(L)
    print("Final L: ", L)

if __name__ == '__main__':
    main()
