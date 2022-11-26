# 일부 구글링한 코드
import sys

C, N = map(int, sys.stdin.readline().rstrip().split())
cities = [
    tuple(map(int,
              sys.stdin.readline().rstrip().split())) for _ in range(N)
]
cities = sorted(cities, key=lambda x: (x[0], x[1]))
INF = int(1e9)
DP = [INF] * (C + 101)
DP[0] = 0

for i in range(N):
    cost, benefit = cities[i]
    for j in range(benefit, C + 101):
        DP[j] = min(DP[j - benefit] + cost, DP[j])

print(min(DP[C:]))