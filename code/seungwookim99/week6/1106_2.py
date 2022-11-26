import sys

C, N = map(int, sys.stdin.readline().rstrip().split())
cities = [
    tuple(map(int,
              sys.stdin.readline().rstrip().split())) for _ in range(N)
]
cities = sorted(cities, key=lambda x: (-(x[1] / x[0]), x[0]))

INF = int(1e9)
DP = [INF] * (C + 101)
DP[0] = 0

for i in range(N):
    cost, benefit = cities[i]
    for j in range(benefit, C + 101):
        if DP[j] > DP[j - benefit] + cost:
            for k in range(benefit + 1):
                DP[j - benefit + k] = min(DP[j - benefit] + cost, DP[j - benefit + k])
print(DP[C])