def shiftVac (xindex, x, E = []):
    vacant = xindex
    xLoc = 0
    while(vacant > 0):
        if(E[vacant -1] <= x):
            xLoc = vacant
            break
        E[vacant] = E[vacant - 1]
        vacant = vacant - 1
        
    return xLoc

def insertionSort(n, E = []):
    for xindex in range(1, n):
        current = E[xindex]
        x = current
        xLoc = shiftVac(xindex, x, E)
        E[xLoc] = current
    return

lists = [1, 4, 5 , 3, 6]
insertionSort(5, lists)
print(lists)