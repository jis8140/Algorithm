def heapSort(n, E = []):
    H = []
    for i in range (n, 0):
        curMax = getMax(H)
        deleteMax(H)
        E[i] = curMax        