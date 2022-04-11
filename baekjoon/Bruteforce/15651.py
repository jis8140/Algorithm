import sys
from itertools import product

# input
N, M = map(int, sys.stdin.readline().split())

# sort and product
answer = sorted(list(product(range(1, N + 1), repeat=M)))

# output
for ele in answer:
    print(*ele)