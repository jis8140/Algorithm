import sys
from collections import deque

# input
n, m = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

# problem solution
que = deque(range(1, n + 1))
answer = 0
while num_list:
    if que[0] != num_list[0] and que.index(num_list[0]) <= len(que) // 2:
        while que[0] != num_list[0]:
            tmp = que.popleft()
            que.append(tmp)
            answer += 1
    else:
        while que[0] != num_list[0]:
            tmp = que.pop()
            que.appendleft(tmp)
            answer += 1

    num_list.pop(0)
    que.popleft()

# output
print(answer)