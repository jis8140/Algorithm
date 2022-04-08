import sys
from itertools import permutations
stdin = sys.stdin.buffer

# input
N, M = map(int, stdin.readline().split())

# 순열을 이용한 수열 찾기
permutation = sorted(list(permutations([x for x in range(1, N + 1)], M)))

# output
for ele in permutation:
    print(*ele)