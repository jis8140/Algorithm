import sys

# input
n = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

# problem solution
dp = [num_list[0]]
for idx in range(1, n):
    dp.append(max(dp[-1] + num_list[idx], num_list[idx]))

# output
print(max(dp))