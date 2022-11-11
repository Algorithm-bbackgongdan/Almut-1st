import heapq
import sys

N, K = map(int, input().split())
jewl = []
bag = []
for _ in range(N):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(jewl, [m, v])

for _ in range(K):
    w = int(input())
    bag.append(w)

# sort by weight
bag.sort()

# 남는거 
heap = []
res = 0

for w in bag:
    while jewl and w >= jewl[0][0]:
        [tempweight, tempval] = heapq.heappop(jewl)
        heapq.heappush(heap, -tempval)
    if heap:
        res -= heapq.heappop(heap)
    elif not jewl:
        break

print(res)