# 촌수계산
# 22.11.2
# bdfs

n = int(input())
start, end = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n
for _ in range(m):
  a, b = map(int,input().split())
  graph[a-1].append(b)
  graph[b-1].append(a)
for node in graph:
  node.sort()
# print(graph)
cnt = 0
flag = False
def dfs(node):
  global flag
  global cnt
  visited[node-1] = True
  cnt +=1
  if node == end:
    flag = True
    print(cnt-1)
    return
  for v in graph[node-1]:
    if visited[v-1] == False:
      dfs(v)
dfs(start)

if not flag:
  print('-1')