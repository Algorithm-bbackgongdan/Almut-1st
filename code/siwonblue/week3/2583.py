# 영역 구하기
# 22.11.2
# dfs

import sys
read=sys.stdin.readline
n,m,k=map(int,read().split())

graph = [[0]*(m) for _ in range(n)]

# 덮기
for _ in range(k):
  a,b,c,d = map(int,read().split())
  for i in range(b,d):
    for j in range(a,c):
      graph[i][j] = 1
    
# for row in graph:
#     print(row)

# 카운트
dx=[-1,0,1,0] 
dy=[0,1,0,-1]
test = 0
test2 = []
def dfs(x,y):
  global test
  if x<0 or y <0 or x>=n or y>=m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = test+1
    test+=1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx,ny)
  else:
    return False
  return True

cnt = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j):
      cnt +=1

for v in graph:
  print(v)