import sys
from bisect import bisect_left

# input
n = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

# problem solution
dp = [num_list[0]]
for idx in range(1, n):
    if dp[-1] < num_list[idx]:
        dp.append(num_list[idx])
    else:
        _idx = bisect_left(dp, num_list[idx])
        dp[_idx] = num_list[idx]

# output
print(len(dp))