import sys

# input
n = int(input())
road = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

# problem solution
price_min = price[0]
price_sum = road[0] * price_min
for idx in range(1, n - 1):
    price_min = min(price_min, price[idx])
    price_sum += price_min * road[idx]

# output
print(price_sum)