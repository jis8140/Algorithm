import sys

# input
n = int(input())
num_list = list(map(int, sys.stdin.readline().split()))

# problem solution
front_len = [1 for _ in range(n)]
back_len = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if num_list[j] < num_list[i]:
            front_len[i] = max(front_len[i], front_len[j] + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if num_list[-j] < num_list[-i]:
            back_len[-i] = max(back_len[-i], back_len[-j] + 1)

max_len = 0
for idx in range(n):
    max_len = max(max_len, front_len[idx] + back_len[idx])

# output
print(max_len - 1)