import sys
sys.setrecursionlimit(10**7)

r,c = map(int,input().split())
visited = [0] * 26
gragh = []
size = 0
for i in range(r):
  gragh.append(list(map(str,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
  global size
  if x< 0 or x >= r or y < 0 or y >= c:
    return 0
  if gragh[x][y] == 'A' and visited[0] == 1:
    return 0
  if gragh[x][y] == 'B' and visited[1] == 1:
    return 0
  if gragh[x][y] == 'C' and visited[2] == 1:
    return 0
  if gragh[x][y] == 'D' and visited[3] == 1:
    return 0
  if gragh[x][y] == 'E' and visited[4] == 1:
    return 0
  if gragh[x][y] == 'F' and visited[5] == 1:
    return 0
  if gragh[x][y] == 'G' and visited[6] == 1:
    return 0
  if gragh[x][y] == 'H' and visited[7] == 1:
    return 0
  if gragh[x][y] == 'I' and visited[8] == 1:
    return 0
  if gragh[x][y] == 'J' and visited[9] == 1:
    return 0
  if gragh[x][y] == 'K' and visited[10] == 1:
    return 0
  if gragh[x][y] == 'L' and visited[11] == 1:
    return 0
  if gragh[x][y] == 'M' and visited[12] == 1:
    return 0
  if gragh[x][y] == 'N' and visited[13] == 1:
    return 0
  if gragh[x][y] == 'O' and visited[14] == 1:
    return 0
  if gragh[x][y] == 'P' and visited[15] == 1:
    return 0
  if gragh[x][y] == 'Q' and visited[16] == 1:
    return 0
  if gragh[x][y] == 'R' and visited[17] == 1:
    return 0
  if gragh[x][y] == 'S' and visited[18] == 1:
    return 0
  if gragh[x][y] == 'T' and visited[19] == 1:
    return 0
  if gragh[x][y] == 'U' and visited[20] == 1:
    return 0
  if gragh[x][y] == 'V' and visited[21] == 1:
    return 0
  if gragh[x][y] == 'W' and visited[22] == 1:
    return 0
  if gragh[x][y] == 'X' and visited[23] == 1:
    return 0
  if gragh[x][y] == 'Y' and visited[24] == 1:
    return 0
  if gragh[x][y] == 'Z' and visited[25] == 1:
    return 0
  
  if gragh[x][y] == 'A':
    visited[0] = 1
  if gragh[x][y] == 'B':
    visited[1] = 1
  if gragh[x][y] == 'C':
    visited[2] = 1
  if gragh[x][y] == 'D':
    visited[3] = 1
  if gragh[x][y] == 'E':
    visited[4] = 1
  if gragh[x][y] == 'F':
    visited[5] = 1
  if gragh[x][y] == 'G':
    visited[6] = 1
  if gragh[x][y] == 'H':
    visited[7] = 1
  if gragh[x][y] == 'I':
    visited[8] = 1
  if gragh[x][y] == 'J':
    visited[9] = 1
  if gragh[x][y] == 'K':
    visited[10] = 1
  if gragh[x][y] == 'L':
    visited[11] = 1
  if gragh[x][y] == 'M':
    visited[12] = 1
  if gragh[x][y] == 'N':
    visited[13] = 1
  if gragh[x][y] == 'O':
    visited[14] = 1
  if gragh[x][y] == 'P':
    visited[15] = 1
  if gragh[x][y] == 'Q':
    visited[16] = 1
  if gragh[x][y] == 'R':
    visited[17] = 1
  if gragh[x][y] == 'S':
    visited[18] = 1
  if gragh[x][y] == 'T':
    visited[19] = 1
  if gragh[x][y] == 'U':
    visited[20] = 1
  if gragh[x][y] == 'V':
    visited[21] = 1
  if gragh[x][y] == 'W':
    visited[22] = 1
  if gragh[x][y] == 'X':
    visited[23] = 1
  if gragh[x][y] == 'Y':
    visited[24] = 1
  if gragh[x][y] == 'Z':
    visited[25] = 1

  size += 1
  for i in range(4):
    dfs(x + dx[i],y + dy[i])
  return size

result = []
cnt = dfs(0,0)
result.append(cnt)
print(result[0])
