import sys

read = sys.stdin.readline

n, m = map(int, read().split())
x, y, direction = map(int, read().split())
board = [list(map(int, read().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
cnt = 1  # 청소 초기횟수
turn = 0  # 각 위치당 회전 초기횟수

# 북,동,남,서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


visited[x][y] = 1  # 첫 위치 방문처리

while True:
    # 회전
    direction -= 1
    if direction == -1:
        direction = 3

    # 다음 위치
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 빈 칸이고, 미방문한 위치이면
    if board[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        cnt += 1
        x, y = nx, ny
        turn = 0
        continue
    # 청소 했거나, 방문한 위치라면 회전
    else:
        turn += 1
    # 회전을 다 했다면 후진
    if turn == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 후진할 수 있는지 확인
        if board[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn = 0

print(cnt)
