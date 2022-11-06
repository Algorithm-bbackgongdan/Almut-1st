# 알파벳
# 22.11.4

import sys
read=sys.stdin.readline
r,c=map(int,read().split())

visited = [[False]*c for _ in range(r)]
visited[0][0]=1
alphabet = [ list(input()) for _ in range(r)]

dx=[-1,0,1,0] 
dy=[0,1,0,-1]
test = []
cnt = 0
ans = 0
def dfs(x,y,cnt):
  global ans
  ans = max(cnt,ans)
  now = alphabet[x][y]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx <0 or ny <0 or nx>=r or ny >=c:
      continue
    if not visited[nx][ny] and alphabet[nx][ny] not in test:
      test.append(alphabet[nx][ny])
      dfs(nx,ny,cnt+1)

dfs(0,0,1)
print(f'ans:{ans}')