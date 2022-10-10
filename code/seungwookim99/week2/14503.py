import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

count = 0
y, x = r, c
dydx = [(0,-1),(1,0),(0,1),(-1,0)]
while True:
  visited[y][x] = True
  ndydx = dydx[4-d:] + dydx[:4-d]

  for i in range(4):
    ny = y + ndydx[i][0]
    nx = x + ndydx[i][1]
    if 0<=ny<N and 0<=nx<M and not visited[ny][nx] and board[ny][nx] == 0:
      y, x = ny, nx
      d = (3+d-i)%4
      break
  else:
    ny = y - ndydx[i][0]
    nx = x - ndydx[i][1]
    if 0<=ny<N and 0<=nx<M and board[ny][nx] == 0:
      y, x = ny, nx
    else:
      break

print(sum([sum(v) for v in visited]))