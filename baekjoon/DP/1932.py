import sys

# input
n = int(input())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# DP를 활용한 bottom-up
for i in range(n-2, -1, -1):
    for j in range(i + 1):
        triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])

# output
print(triangle[0][0])