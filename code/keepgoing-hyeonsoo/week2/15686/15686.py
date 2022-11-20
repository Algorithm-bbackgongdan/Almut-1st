import sys
from itertools import combinations

read = sys.stdin.readline

n, m = map(int, read().split())  # n : 행,열 길이, m : 가게 선택개수

board = [list(map(int, read().split())) for _ in range(n)]

pizzas = []  # 가게 저장 리스트
houses = []  # 집 저장 리스트
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            houses.append((i, j))
        if board[i][j] == 2:
            pizzas.append((i, j))

res = float("inf")
for combi in combinations(pizzas, m):  # combi : 가게 리스트에서 m 개 선택한 결과
    dist = 0  # 현재 선택된 가게 리스트에서의 배달거리
    for house in houses:  # 집 리스트에서 집 하나씩 순회
        temp = float("inf")  # temp : 특정 집에서의 피자배달거리
        for pizza in combi:  # 가게 루프 돌면서 특정 집에서의 배달거리(최소거리) 구함
            temp = min(temp, abs(house[0] - pizza[0]) + abs(house[1] - pizza[1]))
        dist += temp  # 최종 배달거리에 특정 집의 배달거리 누적으로 더함

    # res(현재까지의 최소 배달거리) 와 dist(선택된 가게들에 대한 배달거리) 의 최소 구하기
    res = min(res, dist)

print(res)
