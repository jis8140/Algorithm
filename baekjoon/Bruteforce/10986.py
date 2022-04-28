import sys
from itertools import accumulate
from collections import Counter

# input
n, m = map(int, sys.stdin.readline().split())
num_list = list(map(lambda x: int(x) % m, sys.stdin.readline().split()))

# problem solution
num_accumulate_list = list(accumulate(num_list))
div_list = list(map(lambda x: x % m, num_accumulate_list))
counter = Counter(div_list)
answer = 0

for key in counter.keys():
    if not key:
        answer += counter[key]
    answer += counter[key] * (counter[key] - 1) // 2

# output
print(answer)