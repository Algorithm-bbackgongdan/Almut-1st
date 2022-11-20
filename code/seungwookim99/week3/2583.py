import sys
from collections import deque


def check_boundary(y, x, M, N):
    return 0 <= y < M and 0 <= x < N


def bfs(board, y, x, number):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    q = deque([(y, x)])
    board[y][x] = number
    area = 1
    while q:
        cy, cx = q.popleft()
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if check_boundary(ny, nx, M, N) and board[ny][nx] == 0:
                q.append((ny, nx))
                board[ny][nx] = number
                area += 1
    return area


M, N, K = map(int, sys.stdin.readline().rstrip().split())
board = [[0] * N for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for j in range(y1, y2):
        for i in range(x1, x2):
            board[j][i] = -1

areas = []
count = 1
for i in range(M):
    for j in range(N):
        if board[i][j] == -1 or board[i][j] > 0:
            continue
        else:
            areas.append(bfs(board, i, j, count))
            count += 1

print(count - 1)
areas.sort()
for a in areas:
    print(a, end=" ")