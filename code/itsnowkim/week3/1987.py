from sys import stdin

def dfs(y, x, ans):
    global max_count
    limit = 0

    # move four direction
    for m in range(4):
        i = x + move[m][0]
        j = y + move[m][1]

        # 범위 내
        if i <= -1 or i >= R or j <= -1 or j >= C:
            limit += 1
        else:
            if graph[i][j] not in ans:
                dfs(i, j, ans + graph[i][j])
            else:
                limit += 1
    # 모든 방향 막힘
    if limit == 4:
        max_count = max(max_count, len(ans))

R, C = map(int, stdin.readline().split())

graph = [list(input()) for _ in range(R)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

max_count = 0

dfs(0, 0, graph[0][0])

print(max_count)