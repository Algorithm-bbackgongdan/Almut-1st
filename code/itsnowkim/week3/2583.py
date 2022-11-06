import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x <= -1 or x>= M or y <= -1 or y >= N:
        return False
    if graph[x][y] == 0:
        area[count] += 1
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# input start
M, N, K  = map(int, input().split())

# graph init
graph = [[0] * N for i in range(M)]

# masking block
for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            graph[j][k] = 1

# check visited and calculate area
area = []
count = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            area.append(0)
            if dfs(i,j) == True:
                count += 1

# output area
area.sort()
print(count)
for item in area:
    print(item, end=' ')
