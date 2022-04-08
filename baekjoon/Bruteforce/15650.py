import sys
from itertools import combinations
stdin = sys.stdin.buffer

N, M = map(int, stdin.readline().split())
combination = sorted(list(combinations([x for x in range(1, N + 1)], M)))

for ele in combination:
    print(*ele)