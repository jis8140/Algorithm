import sys

n = int(input())
go = [list(sys.stdin.readline().strip()) for _ in range(n)]

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def search(j: int, i: int):
    global stone_max, ans_j, ans_i
    stone = 0
    for idx in range(8):
        x, y = i + dx[idx], j + dy[idx]
        while x >= 0 and y >= 0 and x < n and y < n:
            if go[y][x] == '.':
                stone = 0
                break
            elif go[y][x] == 'W':
                stone += 1
            elif go[y][x] == 'B':
                break

            x += dx[idx]
            y += dy[idx]

    if stone_max < stone:
        stone_max = stone
        ans_i = i
        ans_j = j
    elif stone_max == stone:
        if ans_i < i:
            ans_i = i
            ans_j = j
        elif ans_i == i:
            ans_j = min(ans_j, j)

stone_max, ans_i, ans_j = 0, n, n
for i in range(n):
    for j in range(n):
        if go[i][j] == '.':
            search(i, j)

if stone_max == 0:
    print('pass')
else:
    print(ans_j, ans_i, sep=' ')
    print(stone_max)