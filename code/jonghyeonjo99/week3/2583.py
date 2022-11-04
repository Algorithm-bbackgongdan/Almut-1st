import sys
sys.setrecursionlimit(10**7)


m,n,k = map(int,input().split())
visited = [[0] * n for i in range(m)]
result = []
graph = [[0] * n for i in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
size = 0

for i in range(k):
  x0,y0,x1,y1 = map(int,input().split())
  for i in range (y0,y1):
    for j in range (x0,x1):
      visited[i][j] = 1

def dfs(x,y):
  global size
  if x< 0 or x >= m or y < 0 or y >= n:
    return 0
  if visited[x][y] == 1:
    return 0
  
  visited[x][y] = 1
  size += 1
  for i in range(4):
    dfs(x + dx[i],y + dy[i])
  return size

for i in range(m):
  for j in range(n):
    cnt = dfs(i,j)
    if cnt != 0:
      result.append(cnt)
      size = 0

result.sort()
print(len(result))
for i in result:
  print(i, end = ' ')


