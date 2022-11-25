# 테스트케이스는 맞는데 틀려서 다시 봐야함...

import sys

read = sys.stdin.readline

r, c = map(int, read().split())
board = []
for _ in range(r):
    board.append(list(read().rstrip()))

check = [0] * 26
check[ord(board[0][0]) - 65] = 1  # 아스키코드값 변환

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maxx = -1


def dfs(x, y, cnt):
    global maxx
    # 상하좌우 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c:  # 범위제한
            if check[ord(board[nx][ny]) - 65] == 0:  # 방문하지 않은 알파벳일때만
                check[ord(board[nx][ny]) - 65] = 1  # check 배열에 알파벳 추가
                ncnt = cnt + 1
                maxx = max(maxx, ncnt)
                dfs(nx, ny, ncnt)
                check[ord(board[nx][ny]) - 65] = 0  # 알파벳 방문 해제처리


dfs(0, 0, 1)

print(maxx)
