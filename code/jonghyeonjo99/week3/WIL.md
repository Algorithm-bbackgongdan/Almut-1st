# 2644 : 촌수계산
## code
```python
def dfs(now,end,num):
  visited[now] = 1
  if now == end:
    result.append(num)
  for i in v[now]:
    if not visited[i]:
      dfs(i,end,num+1)


n = int(input())
x,y = map(int,input().split())
m = int(input())
v = [[] for _ in range(101)]
visited = [0] * (101)
result = []


for i in range (m):
  a,b = map(int,input().split())
  v[a].append(b)
  v[b].append(a) #양방향 간선

dfs(x,y,0)
if len(result) == 0:
  print(-1)
else:
  print(result[0])
```
### 결과
성공
### 접근
시작 정점에서 목표정점까지 깊이 우선 탐색을 돌려야겠다고 생각했다.
시작 정점에서 이웃한 정점으로 넘어갈 때마다 (num + 1)을 해주고,
목표 정점에 도달했을 때 num값을 출력하였다.

## 문제 회고
비교적 빠른시간안에 문제를 해결할 수 있었다.
대표적인 DFS 문제라는 생각이 들었다.
# 2583 : 영역 구하기
### code
```python
import sys
sys.setrecursionlimit(10**7)


m,n,k = map(int,input().split())
visited = [[0] * n for i in range(m)]
result = []
graph = [[0] * n for i in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
size = 0

for i in range(k):
  x0,y0,x1,y1 = map(int,input().split())
  for i in range (y0,y1):
    for j in range (x0,x1):
      visited[i][j] = 1

def dfs(x,y):
  global size
  if x< 0 or x >= m or y < 0 or y >= n:
    return 0
  if visited[x][y] == 1:
    return 0
  
  visited[x][y] = 1
  size += 1
  for i in range(4):
    dfs(x + dx[i],y + dy[i])
  return size

for i in range(m):
  for j in range(n):
    cnt = dfs(i,j)
    if cnt != 0:
      result.append(cnt)
      size = 0

result.sort()
print(len(result))
for i in result:
  print(i, end = ' ')
  ```
### 결과
성공
### 접근
우선 색칠된 직사각형은 배열에서 이미 방문한 곳으로 처리하자는 생각을 제일 먼저 떠올렸다.
이후 남겨진 영역이 몇개로 분리됐는지는 2차 for문을 통해 DFS를 순차적으로 돌려 DFS가 돌아간 횟수로 처리하였다.
각 영역의 DFS에서 정사각형 한칸을 지날 때마다 size += 1을 해주어 영역의 넓이를 구하였다.

## 문제 회고
평소에 DFS 혹은 BFS가 한번만 쓰이는(?) 즉 그래프가 한개인 문제들만 풀다가, 분리된 영역의 개수를 세는 부분 (주어진 그래프 개수를 세는 과정)에서 당황했다. 하나의 그래프 탐색이 끝나면 모두 방문한 것으로 바뀐다는 점을 이용하여 남겨진 영역의 개수를 셀 수 있었다.

또한, 처음에 런타임 에러 (RecursionError)가 떴는데 이를 통해서 파이썬 재귀 최대 깊이 기본설정이 1000회임을 배울 수 있었고, 재귀최대깊이를 다시 설정하는 법을 배울 수 있었다.

지금 코드를 보는데 gragh 배열은 필요가 없어보인다ㅋㅋㅋ
# 2138 : 전구와 스위치
### code
```python
import sys
sys.setrecursionlimit(10**7)

r,c = map(int,input().split())
visited = [0] * 26
gragh = []
size = 0
for i in range(r):
  gragh.append(list(map(str,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
  global size
  if x< 0 or x >= r or y < 0 or y >= c:
    return 0
  if gragh[x][y] == 'A' and visited[0] == 1:
    return 0
  if gragh[x][y] == 'B' and visited[1] == 1:
    return 0
  if gragh[x][y] == 'C' and visited[2] == 1:
    return 0
  if gragh[x][y] == 'D' and visited[3] == 1:
    return 0
  if gragh[x][y] == 'E' and visited[4] == 1:
    return 0
  if gragh[x][y] == 'F' and visited[5] == 1:
    return 0
  if gragh[x][y] == 'G' and visited[6] == 1:
    return 0
  if gragh[x][y] == 'H' and visited[7] == 1:
    return 0
  if gragh[x][y] == 'I' and visited[8] == 1:
    return 0
  if gragh[x][y] == 'J' and visited[9] == 1:
    return 0
  if gragh[x][y] == 'K' and visited[10] == 1:
    return 0
  if gragh[x][y] == 'L' and visited[11] == 1:
    return 0
  if gragh[x][y] == 'M' and visited[12] == 1:
    return 0
  if gragh[x][y] == 'N' and visited[13] == 1:
    return 0
  if gragh[x][y] == 'O' and visited[14] == 1:
    return 0
  if gragh[x][y] == 'P' and visited[15] == 1:
    return 0
  if gragh[x][y] == 'Q' and visited[16] == 1:
    return 0
  if gragh[x][y] == 'R' and visited[17] == 1:
    return 0
  if gragh[x][y] == 'S' and visited[18] == 1:
    return 0
  if gragh[x][y] == 'T' and visited[19] == 1:
    return 0
  if gragh[x][y] == 'U' and visited[20] == 1:
    return 0
  if gragh[x][y] == 'V' and visited[21] == 1:
    return 0
  if gragh[x][y] == 'W' and visited[22] == 1:
    return 0
  if gragh[x][y] == 'X' and visited[23] == 1:
    return 0
  if gragh[x][y] == 'Y' and visited[24] == 1:
    return 0
  if gragh[x][y] == 'Z' and visited[25] == 1:
    return 0
  
  if gragh[x][y] == 'A':
    visited[0] = 1
  if gragh[x][y] == 'B':
    visited[1] = 1
  if gragh[x][y] == 'C':
    visited[2] = 1
  if gragh[x][y] == 'D':
    visited[3] = 1
  if gragh[x][y] == 'E':
    visited[4] = 1
  if gragh[x][y] == 'F':
    visited[5] = 1
  if gragh[x][y] == 'G':
    visited[6] = 1
  if gragh[x][y] == 'H':
    visited[7] = 1
  if gragh[x][y] == 'I':
    visited[8] = 1
  if gragh[x][y] == 'J':
    visited[9] = 1
  if gragh[x][y] == 'K':
    visited[10] = 1
  if gragh[x][y] == 'L':
    visited[11] = 1
  if gragh[x][y] == 'M':
    visited[12] = 1
  if gragh[x][y] == 'N':
    visited[13] = 1
  if gragh[x][y] == 'O':
    visited[14] = 1
  if gragh[x][y] == 'P':
    visited[15] = 1
  if gragh[x][y] == 'Q':
    visited[16] = 1
  if gragh[x][y] == 'R':
    visited[17] = 1
  if gragh[x][y] == 'S':
    visited[18] = 1
  if gragh[x][y] == 'T':
    visited[19] = 1
  if gragh[x][y] == 'U':
    visited[20] = 1
  if gragh[x][y] == 'V':
    visited[21] = 1
  if gragh[x][y] == 'W':
    visited[22] = 1
  if gragh[x][y] == 'X':
    visited[23] = 1
  if gragh[x][y] == 'Y':
    visited[24] = 1
  if gragh[x][y] == 'Z':
    visited[25] = 1

  size += 1
  for i in range(4):
    dfs(x + dx[i],y + dy[i])
  return size

result = []
cnt = dfs(0,0)
result.append(cnt)
print(result[0])

```
### 결과
실패 (메모리 초과)

### 접근
처음 문제를 읽고나서 생각한 아이디어는 알파벳 배열을 만들고, 그래프에서 그 알파벳을 지나면 알파벳 배열에서 그 알파벳을 방문한 것으로 처리하고,
다음 이웃한 정점으로 이동하면서 이동횟수를 cnt에 저장하는 방법이였다.
## 문제회고
위의 접근은 메모리 초과가 발생한 오답이였다.
알파벳 A부터 Z까지 미리 메모리에 할당하는 것이 아니라, 지나간 알파벳만 방문하였다고 저장하는 방법을 찾아봐야겠다.
