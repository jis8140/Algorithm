import sys
from itertools import combinations

# input
n = int(sys.stdin.readline())
score = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

comb_list = list(combinations(range(n), n // 2))
person = set(range(n))

min = sys.maxsize
for comb in comb_list:
    team1 = set(comb)
    team2 = person - team1

    team1_score = 0
    for i in list(team1):
        for j in list(team1):
            team1_score += score[i][j]

    team2_score = 0
    for i in list(team2):
        for j in list(team2):
            team2_score += score[i][j]

    if min > abs(team1_score - team2_score):
        min = abs(team1_score - team2_score)

# output
print(min)

