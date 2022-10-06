n,m = map(int,input().split())
x,y,d = map(int,input().split())
arr = []
for i in range(n):
  arr.append(list(map(int,input().split())))

dx = [0, -1, 0, 1] 
dy = [-1, 0, 1, 0]

arr[x][y] = 1 #시작위치 카운트
cnt = 1

while (True):
  flag = 0
  for i in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    if d == 0:
      d = 3
    elif d == 3:
      d = 2
    elif d == 2:
      d = 1
    elif d == 1:
      d = 0
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
      arr[nx][ny] = 1
      cnt += 1
      flag = 1
      x = nx
      y = ny
      break
  if flag == 0:
    nx = x - dx[d]
    ny = y - dy[d]
    if arr[nx][ny] == 0:
        x = nx
        y = ny
    else:
        print(cnt)
        break
