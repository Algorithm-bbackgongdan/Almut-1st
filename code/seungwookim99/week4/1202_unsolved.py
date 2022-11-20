import sys
import heapq
from bisect import bisect_left

N, K = map(int, sys.stdin.readline().rstrip().split())
Jew = []
for _ in range(N):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(Jew, (-v, m))
Bag = [int(sys.stdin.readline().rstrip()) for _ in range(K)]
Bag = sorted(Bag)

res = 0
while Jew and Bag:
    v, m = heapq.heappop(Jew)
    idx = bisect_left(Bag, m)
    if idx == len(Bag):  # 못담음
        continue
    res += abs(v)
    del Bag[idx]

print(res)