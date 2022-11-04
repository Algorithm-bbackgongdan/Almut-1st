def dfs(now,end,num):
  visited[now] = 1
  if now == end:
    result.append(num)
  for i in v[now]:
    if not visited[i]:
      dfs(i,end,num+1)


n = int(input())
x,y = map(int,input().split())
m = int(input())
v = [[] for _ in range(101)]
visited = [0] * (101)
result = []


for i in range (m):
  a,b = map(int,input().split())
  v[a].append(b)
  v[b].append(a) #양방향 간선

dfs(x,y,0)
if len(result) == 0:
  print(-1)
else:
  print(result[0])