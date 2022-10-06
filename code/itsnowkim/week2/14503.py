def turn_left(d):
  #0인 경우에는 북쪽을, 1인 경우에는 동쪽을, 2인 경우에는 남쪽을, 3인 경우에는 서쪽
  if d == 0 :
    return 3
  elif d == 1:
    return 0
  elif d == 2:
    return 1
  elif d ==3:
    return 2

n,m = map(int,input().split())
r,c,d = map(int,input().split())

# map
graph = []
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

cnt = 1
visited[r][c] = 1

d = (d+1)%4

while 1:
  flag = 0
  
  for _ in range(4):
    d = turn_left(d)

    nx = r + dx[d]
    ny = c + dy[d]

    # 범위 내 index 위치 & 청소하지 않은 부분
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
      if visited[nx][ny] == 0:
        visited[nx][ny] = 1
        cnt += 1
        
        # 이동
        r = nx
        c = ny

        flag = 1
        break

  if flag == 0:
    # 후진
    if graph[r-dx[d]][c-dy[d]] == 1:
      print(cnt)
      break
    else:
      r = r-dx[d]
      c = c-dy[d]






