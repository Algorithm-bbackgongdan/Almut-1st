# 로봇 청소기
# 22.10.3
# 구현

n, m = map(int, input().split())
d = [[0]*m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1
data = [list(map(int,input().split())) for _ in range(n)]
cnt = 1

# 이동 세팅
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    if direction == 0:
        direction = 3
        return
    direction -= 1

def solve(data,x,y):
    global cnt
    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 벽이 아니고 청소안한 것
        if data[nx][ny] == 0 and d[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            cnt +=1
            turn_time = 0
        # 벽이 아니고 청소한 것
        else:
            # print('벽이 아니고 청소한 것')
            # print('벽이고 청소한 것')
            # print('벽이고 청소 안 한 것')
            turn_time +=1
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if data[nx][ny] == 0:
                x = nx
                y = ny
                turn_time = 0
            else:
                break
    print(cnt)
solve(data,x,y)


