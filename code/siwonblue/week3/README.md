### 📌 문제 출처

- [백준] 2644번 : 촌수계산
- [원글 링크](https://www.acmicpc.net/problem/2644)

### ❓예제입력

```
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
```

```
9
8 6
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6
```

### ‼️접근 방식

- BFS 로 처음 접근해서 풀었다가 개수를 세기가 힘들다는 점을 깨닫고
- DFS 로 바꿨음
- 단순 DFS 를 구현했는데 테스트 케이스를 통과했는데 제출은 실패뜸
- 그 이유를 못 찾고 있음

### 🔎 알고리즘 및 코드 구현

```python

n = int(input())
start, end = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n
for _ in range(m):
  a, b = map(int,input().split())
  graph[a-1].append(b)
  graph[b-1].append(a)
for node in graph:
  node.sort()
# print(graph)
cnt = 0
flag = False
def dfs(node):
  global flag
  global cnt
  visited[node-1] = True
  cnt +=1
  if node == end:
    flag = True
    print(cnt-1)
    return
  for v in graph[node-1]:
    if visited[v-1] == False:
      dfs(v)
dfs(start)

if not flag:
  print('-1')
```

### 🕰 시간분석

- 해당 코드의 시간:
  O(N)
- 판단한 이유:
  dfs 는 선형 시간

### ✔️ 예외처리

### ⚔️ 코드 스니펫 및 내장 모듈

```python
# 코드 스니펫
start, end = map(int,input().split())
```

```python
# 내장 모듈
```

### ☑︎ 회고

> 접근 방식에 써뒀는데 bfs 로 먼저 다가갔고 노드 한 칸씩 이동할 때마다 개수를 세기 위해서는
> dfs 가 적절하다는 것을 깨닫고 고쳤다. 근데 테스트 케이스를 통과했는데 문제는 틀린다. 어느 부분에서
> 틀리는지 확인을 못 하는 중.


----

### 📌 문제 출처

- [BOJ] 2583 : 영역 구하기
- [원글 링크](https://www.acmicpc.net/problem/2583)

### ❓예제입력
```
5 7 3
0 2 4 4
1 1 2 5
4 0 6 2
```

### ‼️접근 방식

- 직사각형 놓기
- 넓이 계산

### 🔎 알고리즘 및 코드 구현

```python
# 영역 구하기
# 22.11.2
# dfs

import sys
read=sys.stdin.readline
n,m,k=map(int,read().split())

graph = [[0]*(m) for _ in range(n)]

# 덮기
for _ in range(k):
  a,b,c,d = map(int,read().split())
  for i in range(b,d):
    for j in range(a,c):
      graph[i][j] = 1
    
# for row in graph:
#     print(row)

# 카운트
dx=[-1,0,1,0] 
dy=[0,1,0,-1]
test = 0
test2 = []
def dfs(x,y):
  global test
  if x<0 or y <0 or x>=n or y>=m:
    return False
  if graph[x][y] == 0:
    graph[x][y] = test+1
    test+=1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      dfs(nx,ny)
  else:
    return False
  return True

cnt = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j):
      cnt +=1

for v in graph:
  print(v)

```

### 🕰 시간분석

- 해당 코드의 시간:
O(N)
- 판단한 이유:
DFS 는 선형 시간

### ✔️ 예외처리

### ⚔️ 코드 스니펫 및 내장 모듈

```python
# 코드 스니펫
```

```python
# 내장 모듈
```

### ☑︎ 회고
> 개수는 세었는데, 넓이는 구하지 못 함.
>