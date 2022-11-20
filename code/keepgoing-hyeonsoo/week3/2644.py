import sys
from collections import deque

read = sys.stdin.readline

n = int(read())
a, b = map(int, read().split())
m = int(read())

graph = {}

for i in range(1, n + 1):
    graph[i] = []

# 그래프 생성
for _ in range(m):
    i, j = map(int, read().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (n + 1)  # 방문처리용 배열
distance = [0] * (n + 1)  # 시작점부터의 거리계산용 배열

# bfs
def bfs(start):
    # 첫 노드 큐에 담고 방문처리
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        for node in graph[v]:  # 인접노드들 방문
            # 방문하지 않은 노드일때만 방문처리 후 거리 증가시키기
            if visited[node] == 0:
                q.append(node)
                visited[node] = 1
                distance[node] = distance[v] + 1


bfs(a)

if visited[b] == 0:  # 방문 안 한 노드라면 촌수 계산 불가
    print(-1)
else:
    print(distance[b])
