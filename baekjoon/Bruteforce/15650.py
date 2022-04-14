import sys
from itertools import combinations
stdin = sys.stdin.buffer

# input
N, M = map(int, stdin.readline().split())

# method_1
combination = sorted(list(combinations([x for x in range(1, N + 1)], M)))

# output
for ele in combination:
    print(*ele)

# method_2
def backtrack(prevalue, start, size):
    if size == M:
        result.append(prevalue)
        return

    for idx in range(start + 1, N + 1):
        backtrack(prevalue + [str(idx)], idx, size + 1)

result = list()
for idx in range(1, N + 1):
    backtrack([str(idx)], idx, 1)

# output
print('\n'.join(list(map(' '.join, sorted(result)))))