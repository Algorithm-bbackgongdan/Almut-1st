import heapq
import sys

dia = []
bag = []
res = 0

n,k = map(int,sys.stdin.readline().split())

for i in range (n):
  heapq.heappush(dia, list(map(int, sys.stdin.readline().split())))

for i in range(k):
  bag.append(int(sys.stdin.readline()))

bag.sort()
temp = []

for i in (bag):
  while dia and i >= dia[0][0]:
    heapq.heappush(temp,-heapq.heappop(dia)[1])
  if temp:
    res -= heapq.heappop(temp)
  elif not dia:
    break

print(res)