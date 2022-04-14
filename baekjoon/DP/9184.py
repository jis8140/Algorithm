import sys
from collections import defaultdict

dp = defaultdict(int)

def w(a, b, c):
    global dp
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        if (20, 20, 20) not in dp:
            dp[(20, 20, 20)] = w(20, 20, 20)
            return dp[(20, 20, 20)]
        else:
            return dp[(20, 20, 20)]

    if a < b and b < c:
        if (a, b, c - 1) not in dp:
            dp[(a, b, c - 1)] = w(a, b, c - 1)
        if (a, b - 1, c - 1) not in dp:
            dp[(a, b - 1, c - 1)] = w(a, b - 1, c - 1)
        if (a, b - 1, c) not in dp:
            dp[a, b - 1, c] = w(a, b - 1, c)
        return dp[(a, b, c - 1)] + dp[(a, b - 1, c - 1)] - dp[(a, b - 1, c)]

    if (a-1, b, c) not in dp:
        dp[(a-1, b, c)] = w(a-1, b, c)
    if (a-1, b-1, c) not in dp:
        dp[(a-1, b-1, c)] = w(a-1, b-1, c)
    if (a - 1, b, c-1) not in dp:
        dp[(a-1, b, c-1)] = w(a-1, b, c-1)
    if (a-1, b-1, c-1) not in dp:
        dp[(a-1, b-1, c-1)] = w(a-1, b-1, c-1)
    return dp[(a-1, b, c)] + dp[(a-1, b-1, c)] + dp[(a-1, b, c-1)] - dp[(a-1, b-1, c-1)]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break

    dp[(a, b, c)] = w(a, b, c)
    print('w(', a, ', ', b, ', ', c, ') = ', dp[(a, b, c)], sep='')