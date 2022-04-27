import sys
from bisect import bisect_left

# input
n = int(input())
power_pole = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# problem solution
power_pole.sort(key=lambda x: (x[0], x[1]))
pole_list = [y for x, y in power_pole]

dp = [pole_list[0]]
for i in range(1, n):
    if dp[-1] < pole_list[i]:
        dp.append(pole_list[i])
    else:
        idx = bisect_left(dp, pole_list[i])
        dp[idx] = pole_list[i]

# output
print(n - len(dp))