import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())

print("\n".join(list(map(' '.join, combinations_with_replacement([str(x) for x in range(1, N + 1)], M)))))