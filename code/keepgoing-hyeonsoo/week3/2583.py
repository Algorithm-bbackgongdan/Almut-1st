import sys

sys.setrecursionlimit(10**6)  # 재귀횟수 제한 증가

read = sys.stdin.readline

m, n, k = map(int, read().split())
board = [[0] * n for _ in range(m)]

# board판 만들기
for _ in range(k):
    a, b, c, d = map(int, read().split())
    for i in range(b, d):
        for j in range(a, c):
            board[i][j] = 1  # 직사각형 칠해져 있으면 1로 표시

visited = [[0] * n for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
res = []


def dfs(x, y):
    global cnt  # 해당 영역의 넓이
    visited[x][y] = 1
    cnt += 1  # dfs 실행될 때마다 넓이 1씩 증가
    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:  # 범위제한
            # board 0 이면서 미방문한 영역만 dfs
            if board[nx][ny] == 0 and visited[nx][ny] == 0:
                dfs(nx, ny)


for i in range(m):
    for j in range(n):
        if board[i][j] == 0 and visited[i][j] == 0:
            cnt = 0
            dfs(i, j)
            res.append(cnt)

res.sort()
print(len(res))
print(" ".join(map(str, res)))
