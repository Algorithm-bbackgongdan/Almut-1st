# 시간 초과

import sys
from itertools import combinations

read = sys.stdin.readline

n = int(read())
lst = sorted(list(map(int, read().split())))

tmp = float("inf")

for combi in combinations(lst, 2):
    if abs(sum(combi)) < tmp:
        tmp = abs(sum(combi))
        res = combi

res = sorted(list(res))
print(res[0], res[1])
