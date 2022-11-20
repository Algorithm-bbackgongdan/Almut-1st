import sys
import heapq
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
Jew = []
for _ in range(N):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    Jew.append((m, v))
Bag = deque(int(sys.stdin.readline().rstrip()) for _ in range(K))
Bag = sorted(Bag) # 가방 용량으로 정렬
Jew = sorted(Jew, key=lambda x: (x[0])) # 보석 무게로 정렬

candidate = []

res = 0
b_i, j_i = 0, 0 # 가방, 보석을 순회하는 인덱스
while b_i < K and j_i < N:
    b = Bag[b_i] # 현재 가방
    while j_i < N and b >= Jew[j_i][0]:
				# 현재 가방으로 담을 수 있는 보석들을 전부 heap에 push
        heapq.heappush(candidate, -Jew[j_i][1]) # 가격에 대한 Max heap
        j_i += 1
    if j_i >= N: # 모든 보석을 순회했다면
        while candidate and b_i < K: # 남은 가방들에 대해 보석을 전부 담음
            res += abs(heapq.heappop(candidate)) # 가장 큰 값의 보석 담음
            b_i += 1
        break
    if candidate:
        res += abs(heapq.heappop(candidate)) # 가장 큰 값의 보석 담음
    b_i += 1 # 다음 가방

print(res)