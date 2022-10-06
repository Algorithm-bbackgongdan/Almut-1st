from itertools import combinations
import sys


def get_chicken_distance(chicken, house):
    answer = 0
    for h in house:
        min_num = int(1e10)
        for c in chicken:
            tmp = abs(h[0] - c[0]) + abs(h[1] - c[1])
            min_num = min(min_num, tmp)
        answer += min_num
    return answer


n, m = map(int, sys.stdin.readline().rstrip().split())
total_chicken = []
house = []
for y in range(n):
    tmp = list(map(int, sys.stdin.readline().rstrip().split()))
    for x in range(n):
        if tmp[x] == 1:
            house.append([y, x])
        elif tmp[x] == 2:
            total_chicken.append([y, x])

answer = int(1e10)
for l in range(1, m + 1):
    for chicken in combinations(total_chicken, l):
        chicken_distance = get_chicken_distance(chicken, house)
        answer = min(answer, chicken_distance)
print(answer)
