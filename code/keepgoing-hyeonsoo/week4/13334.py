# 1931 과 약간 비슷
# minheap 을 이용

import heapq
import sys

read = sys.stdin.readline

n = int(read())
lst = [sorted(list(map(int, read().split()))) for _ in range(n)]  # 정렬 한 채로 추가
# print(lst)
# [[5, 40], [25, 35], [10, 20], [10, 25], [30, 50], [50, 60], [25, 30], [80, 100]]

lst.sort(key=lambda x: (x[1], x[0]))  # 두 번째 원소(끝 위치) 기준으로 정렬
# print(lst)
# [[10, 20], [10, 25], [25, 30], [25, 35], [5, 40], [30, 50], [50, 60], [80, 100]]

d = int(input())  # 철로 길이

result = -1
heap = []
for s, e in lst:
    if e - s <= d:  # 철로 길이 안에 들어오면 시작점만 heap에 push
        heapq.heappush(heap, s)
    while heap and d < e - heap[0]:  # 끝점과 왼쪽의 최솟값이 철로에 포함이 안 된다면 그 값은 heap 에서 pop 시킴
        heapq.heappop(heap)
    result = max(result, len(heap))
print(result)
