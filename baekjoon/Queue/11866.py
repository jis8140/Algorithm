import sys
from collections import deque

# input
n, m = map(int, sys.stdin.readline().split())

# problem solution
q = deque(range(1, n + 1))
sequence = list()

while q:
    for _ in range(m - 1):
        tmp = q.popleft()
        q.append(tmp)
    sequence.append(q.popleft())

# output
print("<" + ", ".join(map(str, sequence)) + ">")