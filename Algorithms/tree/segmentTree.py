import sys
INPUT = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = [0] * (4 * len(INPUT))

def init(start: int, end:int, index: int) -> int:
    if start == end:
        tree[index] = INPUT[start]
        return tree[index]

    mid = (start + end) // 2
    tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return tree[index]

def query(start: int, end: int, index: int, q_left:int, q_right: int) -> int:
    if q_left > end or q_right < start:
        return 0

    if q_left <= start and q_right >= end:
        return tree[index]

    mid = (start + end) // 2
    return query(start, mid, index*2, q_left, q_right) + query(mid + 1, end, index*2 + 1, q_left, q_right)

init(0, 9, 1)
s, e = map(int, sys.stdin.readline().split())
print(query(0, 9, 1, s, e))