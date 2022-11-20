import sys

def dfs(board, curr, end, visited, count):
    if curr == end:
        print(count)
        return True
    visited[curr] = True
    count += 1
    isPossible = False
    for i in board[curr]:
        if not visited[i]:
            isPossible = isPossible or dfs(board, i, end, visited, count) #bit 연산 or
    return isPossible

N = int(sys.stdin.readline().rstrip())
start, end = map(int, sys.stdin.readline().rstrip().split())
M = int(sys.stdin.readline().rstrip())
board = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    board[x].append(y)
    board[y].append(x)

visited = [False] * (N + 1)
isPossible = dfs(board, start, end, visited, 0)
if not isPossible:
    print(-1)