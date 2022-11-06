import sys
R, C = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(lambda x : ord(x) - ord('A'), sys.stdin.readline().rstrip())) for _ in range(R)]
visited = [0]*26
visited[board[0][0]] = 1
MAX_NUM = 1
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs(y,x,R,C,count):
  global MAX_NUM
  MAX_NUM = max(MAX_NUM, count)
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0 <= ny < R and 0 <= nx < C and visited[board[ny][nx]] == 0:
      visited[board[ny][nx]] = 1
      dfs(ny,nx,R,C,count+1)
      visited[board[ny][nx]] = 0
  return
dfs(0,0,R,C,1)
print(MAX_NUM)