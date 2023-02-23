
arr = [[1, 2, 3, 4],
       [2, 3, 4, 5],
       [3, 4, 5, 6],
       [4, 5, 6, 7]]


prefix_sum = [[0 for _ in range(len(arr[0]))] for _ in range(len(arr))]

for i in range(1, len(arr) + 1):
    for j in range(1, len(arr[0]) + 1):
        prefix_sum[i][j] = arr[i - 1][j - 1] + \
            prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j]
