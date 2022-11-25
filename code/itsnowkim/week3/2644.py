import sys

def dfs(node):
    # 찾음
    if node == p2:
        print(visited[p2])
        sys.exit()
    # 첫 방문일 경우만
    for next in graph[node]:
        if visited[next] == 0:
            # 현재 노드에 방문 횟수 + 1
            visited[next] = visited[node] + 1
            dfs(next)

n = int(input())
# sparse matrix
graph = [[] for _ in range(n+1)]
p1, p2 = map(int, input().split())

# max relation
rel = int(input())

# visited check
visited = [0]*(n+1)

# construct graph
for _ in range(rel):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# call dfs
dfs(p1)
print(-1)