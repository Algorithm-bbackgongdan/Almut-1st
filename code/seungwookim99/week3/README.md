# Week 3
3주차에 대한 WIL

# 2644 : 촌수계산
## 😎 Solved Code

### 💻 Code

```python
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
```

### ❗️ 결과

성공

### 💡 접근

촌수 관계를 트리 형태로 나타낼 수 있다. 하지만 탐색시에는 방향이 정해져있지 않기 때문에 방향이 없는 비순환 구조의 그래프라 생각하고 풀고자 했다. 그래프 구조로 촌수를 표현하고 나면 시작 노드부터 끝 노드까지 경로는 단 하나만 존재한다. 따라서 단순히 DFS를 이용해 문제를 해결하면 될 것이다. DFS를 사용하며 count값을 증가시키며 몇 촌인지 계산했다.

만약 촌수를 구할 수 없다면, 즉, 그래프 사이의 간선이 부재하여 그래프가 분리되어있어 순회가 불가능하면 -1을 출력해야한다. 이를 위해 DFS를 이용한 순회 결과 끝 노드까지 도달하지 못했다는 것을 알려야 한다. 이를 위해 촌수 계산 성공시(끝 노드 도달시) `return True`를 하고, `False` 로 초기화된 `isPossible` 이라는 변수와 함께 재귀 호출시에 `isPossible = isPossible or dfs(…)` (bit 연산 or)을 이용해 한 번이라도 촌수계산 성공시 dfs는 반드시 `True`를 반환하도록 처리했다.

## 🥳 문제 회고

기본적인 자료구조 사용과 DFS 순회 문제였다. 인접행렬만 사용하다가 연습겸 연결리스트를 사용해 구현했다.

# 2583: 영역 구하기
## 😎 Solved Code

### 💻 Code

```python
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
```

### ❗️ 결과

성공

### 💡 접근

우선 모눈종이를 전부 0으로 초기화 한다. 구분을 위해 직사각형이 놓인 공간은 -1 로 값을 바꾼다. 그럼 문제를 해결할 준비를 마쳤다.

분리된 영역들의 값은 전부 0인데, 번호를 매기며 영역들을 구분할 것이다. (0,0) 부터 (N,M)까지  순회하며 board[y][x] == 0 이라면 BFS를 이용해 인접한 영역들(0인 영역)을 count로 채워준다. BFS 작업을 마치면 count += 1 을 한다. 이렇게 하면 분리된 영역들이 1, 2, 3, … 으로 분리가 된다.

BFS 내부에서는 queue에 넣을 때마다 area += 1 을 하며 영역을 더해나간다.

## 🥳 문제 회고

전형적인 BFS 유형중 하나였던 것 같다. 2차원 공간에서 서로 떨어진 면적을 구하거나, 서로 떨어진 영역의 개수를 세는 컨셉의 문제는 대부분 BFS로 풀렸던 것 같다. 아래는 내가 생각하는 좋은 BFS 문제다. 아래 문제들로부터 이번 문제와 같이 유사한 컨셉의 BFS 문제를 쉽게 해결할 수 있었다.

- 경쟁적 전염 : [https://www.acmicpc.net/problem/18405](https://www.acmicpc.net/problem/18405)
- 연구소 : [https://www.acmicpc.net/problem/14502](https://www.acmicpc.net/problem/14502)

# 1987 : 알파벳
## 🥺 Unsolved Code

### 💻 Code

```python
import sys

MAX_NUM = 0
R, C = map(int, sys.stdin.readline().rstrip().split())
board = []
chars = dict()
for _ in range(R):
    line = list(sys.stdin.readline().rstrip())
    for c in line:
        chars[c] = True
    board.append(line)

def check_boundary(y, x, R, C):
    return 0 <= y < R and 0 <= x < C

def dfs(y, x, R, C, count):
    global MAX_NUM
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    MAX_NUM = max(MAX_NUM, count)
    chars[board[y][x]] = False
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if check_boundary(ny, nx, R, C) and chars[board[ny][nx]]:
            dfs(ny, nx, R, C, count + 1)
    chars[board[y][x]] = True
    return

dfs(0, 0, R, C, 1)
print(MAX_NUM)
```

### ❗️ 결과

실패

### 💡 접근

얼핏 보기에 DFS로 금방 해결할 수 있을 것 같다. 하지만 유난히 낮은 정답률의 골드 4 문제인 만큼 함정이 숨어있을 것이다. 

중요한 조건 - `지금까지 지나온 알파벳은 다시 등장하면 안된다` 

위의 조건을 말을 이동할 때 마다 확인해야하는데 시간복잡도가 O(1) 이어야 한다. 안그래도 DFS 완전탐색이라 시간복잡도가 exponential 한데, 위 조건을 O(n)으로 단순하게 처리하면 안된다.

따라서 나는 dictionary를 썼다. dictionary는 key-value 형태의 자료구조라 O(1)에 값을 조회할 수 있다.

```python
{'C': True, 'A': True, 'B': True, 'D': True}
```

요런식으로 처음 입력을 받을 때 dictionary를 만들고, 말을 움직일 때 마다 해당 위치의 alphabet을 key로 하는 dictionary의 value를 False로 바꿔준다. 예를 들어, (0,0) 시작점이 C라면 dfs 시작시에 아래와 같이 바뀐다.

```python
{'C': False, 'A': True, 'B': True, 'D': True}
```

상하좌우 모든 방향에 대해 탐색이 끝나면 다시 True로 되돌려 놓는다.

그런데… 분명 테스트 케이스는 다 통과하는데. pypy로 채점시 60% 정도에서 시간 초과가 뜬다.

아직 뭐가 문제인지 잘 모르겠다ㅠ

## 😎 Solved Code

```python
import sys
R, C = map(int, sys.stdin.readline().rstrip().split())
board = [list(map(lambda x : ord(x) - ord('A'), sys.stdin.readline().rstrip())) for _ in range(R)]
visited = [0]*26
visited[board[0][0]] = 1
MAX_NUM = 1
dy = [0,1,0,-1]
dx = [1,0,-1,0]
def dfs(y,x,R,C,count):
  global MAX_NUM
  MAX_NUM = max(MAX_NUM, count)
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if 0 <= ny < R and 0 <= nx < C and visited[board[ny][nx]] == 0:
      visited[board[ny][nx]] = 1
      dfs(ny,nx,R,C,count+1)
      visited[board[ny][nx]] = 0
  return
dfs(0,0,R,C,1)
print(MAX_NUM)
```

### ❗️ 결과

성공

(위 풀이는 6개월 전의 내가 푼 것이다. 따라서 현재의 나는 퇴보해서 해결 못했다ㅎㅎ)

### 💡 접근

처음 접근이랑 비슷하다. 이미 지나온 알파벳을 O(1)에 조회하기 위해 이번에는 list를 썼다. ord(x) - ord(’A’)를 사용해서 A~Z 까지 0부터 순서대로 정수를 mapping 해서 list의 index를 쓴 것이다.

즉 이전 풀이와 비교해보면

- dictionary key (이전) (ex. A,B,C,…) == list index (현재) (ex. 0,1,2,…)
- dictionary value (이전) == list element value (현재) ← 둘 다 방문 여부를 나타냄 (True / False)

 이 외에는 큰 차이가 없다.

## 🥳 문제 회고

아직 왜 틀렸는지 잘 모르겠다. 예상하건대 실패 코드에서

```python
R, C = map(int, sys.stdin.readline().rstrip().split())
board = []
chars = dict()
for _ in range(R):
    line = list(sys.stdin.readline().rstrip()) 
    for c in line:        # <- 요부분 의심스러움
        chars[c] = True
    board.append(line)
```

dictionry 생성을 위해 line마다 순회하며 alphbet을 넣어주는데, 이 과정에서 연산 시간이 더해져서 시간 초과가 발생하지 않았나… 하는 생각도 든다. 좀 더 공부해봐야 확실히 알 것 같다.