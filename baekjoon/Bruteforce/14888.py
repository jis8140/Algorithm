# import sys
# from itertools import permutations
# stdin = sys.stdin.buffer
#
# # input
# n = int(stdin.readline())
# num_list = list(map(int, stdin.readline().split()))
# operator_num = list(map(int, stdin.readline().split()))
#
# operator = ''.join([str(idx) * val for idx, val in enumerate(operator_num)])
# operator_list = list(permutations(operator, n - 1))
#
# result = list()
# for operators in operator_list:
#     res = num_list[0]
#     for idx in range(n - 1):
#         if operators[idx] == '0':
#             res += num_list[idx + 1]
#         elif operators[idx] == '1':
#             res -= num_list[idx + 1]
#         elif operators[idx] == '2':
#             res *= num_list[idx + 1]
#         else:
#             if res < 0:
#                 res = -((-res) // num_list[idx + 1])
#             else:
#                 res //= num_list[idx + 1]
#     result.append(res)
#
# # output
# print(max(result))
# print(min(result))

import sys
stdin = sys.stdin.buffer

n = int(stdin.readline())
num_list = list(map(int, stdin.readline().split()))
operator = list(map(int, stdin.readline().split()))

max = -sys.maxsize
min = sys.maxsize
# backtrack
def backtrack(pre_value, size, add, sub, mul, div):
    global max, min
    if size == n - 1:
        if max < pre_value:
            max = pre_value

        if min > pre_value:
            min = pre_value

    if add:
        backtrack(pre_value + num_list[size + 1], size + 1, add - 1, sub, mul, div)
    if sub:
        backtrack(pre_value - num_list[size + 1], size + 1, add, sub - 1, mul, div)
    if mul:
        backtrack(pre_value * num_list[size + 1], size + 1, add, sub, mul - 1, div)
    if div:
        if pre_value < 0:
            backtrack(-(abs(pre_value) // num_list[size + 1]), size + 1, add, sub, mul, div - 1)
        else:
            backtrack(pre_value // num_list[size + 1], size + 1, add, sub, mul, div - 1)
backtrack(num_list[0], 0, *operator)
print(max, min, sep="\n")