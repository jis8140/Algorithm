import sys
from itertools import accumulate

# input
n, m = map(int, sys.stdin.readline().split())
num_list = [list(accumulate(list(map(int, sys.stdin.readline().split())))) for _ in range(n)]

# problem solution
for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    ans = 0
    for i in range(x1-1, x2):
        if y1 == 1:
            ans += num_list[i][y2 - 1]
        else:
            ans += num_list[i][y2 - 1] - num_list[i][y1 - 2]

    print(ans)