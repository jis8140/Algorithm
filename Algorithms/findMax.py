def find_max(n, E = []):
    max = E[0]
    for index in range(1,n):
        if ( E[index] > max ):
            max = E[index]
    return max