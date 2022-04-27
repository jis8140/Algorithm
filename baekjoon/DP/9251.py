import sys

# input
a_string = sys.stdin.readline().strip()
b_string = sys.stdin.readline().strip()

# problem solution
n = len(a_string)
k = len(b_string)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n + 1):
    for j in range(k + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif a_string[i - 1] == b_string[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# output
print(dp[-1][-1])