# Week2

# [BOJ] 15686 : 치킨 배달

### 📌 문제 출처
- [BOJ] 15686 : 치킨 배달
- [해당 문제 링크](https://www.acmicpc.net/problem/15686)

### ❓예제입력

```text
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
```

### ‼️접근 방식

- 치킨집과 집의 위치를 모두 파악
- 위치 정보를 이용하여 각 집마다 치킨 집과의 거리를 모두 파악
- 치킨 집이 x 개가 있고 m 개만 남겨야 한다면
- 나올 수 있는 치킨 집의 개수는 xCm 개가 된다 (itertools 모듈 사용)
- 그 각각의 경우의 수에 대해 모두 거리를 구하고 최소 값을 모은 다음 그 중에서 다시 최소값 찾기

### ✔️ 코드 구현 및 알고리즘

```python
# 치킨 배달
# 22.10.4
# 구현

from itertools import combinations

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# 치킨 집과 집 넣어 주면 도시의 치킨 거리 출력해주는 함수
def city_distance(home,bbq):
    city = []
    for a in home:
        test = []  # 집에서 모든 치킨 집에 대한 거리
        for b in bbq:
            test.append(abs(a[0] - b[0]) + abs(a[1] - b[1]))
        # print('test',test)
        city.append(min(test))  # 치킨 거리
    return sum(city)  # 도시의 치킨 거리

def solve(data):
    # 치킨집과 집의 위치 인덱스 뽑아내기
    bbq = []
    home = []
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            if v == 1:
                home.append([i+1,j+1])
            elif v == 2:
                bbq.append([i+1,j+1])
    # print('치킨집 위치',bbq)
    # print('집 위치',home)

    # 치킨집이 x 개가 있고 m 개만 남겨야 하면
    # 나올 수 있는 치킨 집의 개수는 xCm 개가 된다.
    # 그 각각의 경우의 수에 대해 모두 거리를 구하고 최소값을 모으고 그 중 다시 최소값 찾기

    # 남길 치킨 집 경우의 수
    lists = list(combinations(bbq,m))
    res = []
    for one in lists:
        # print('combination : ',a)
        res.append(city_distance(home, one))
    print(min(res)) # len([17, 18, 15, 10, 22, 21, 15, 22, 17, 17]) == xCm
solve(data)
```

### 🕰 시간분석

맵의 크기가 50x50 이 최대이고 치킨 집의 개수는 최대 13 이다.

`def solve()` 와 `def city_distance()` 에서 각각 이중 반복문이 나와서 시간 복잡도는 $`O(N^2)`$ 이 된다. 파이썬은 이차 시간일 경우 입력의 크기가 2,000 정도면 1초 시간제한을 통과할 수 있기 때문에 시간은 충분한 코드다. 아래를 암기해두면 좋다. 1초 기준으로 입력받을 수 있는 데이터의 크기와 가능한 시간 복잡도이다.

| N의 범위 | 시간 복잡도   |
| --- |----------|
| 500 | 3차 시간    |
| 2,000 | 2차 시간    |
| 100,000 | 로그 선형 시간 |
| 10,000,000 | 선형 시간    |

### ✔ 예외처리

입력 예제만 다 돌려보고 맞길래 그냥 제출했는데 정답이라 끝났다.

### ⚔️ 내장 모듈 및 코드 스니펫

```python
# 조합 모듈
from itertools import combinations 
test = [1,2,3]
result = list(cominations(test,2)) # 3C2 , [(1,2),(1,3)(2,3)]
```

```python
# 입력 코드 스니펫
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
```

### ☑︎ 회고

중간에 막혔는데 차분하게 생각을 정리하고 필요한 부분을 짚어낸 다음에 그 부분만 집중적으로 구현하여 문제를 해결할 수 있었다. 특히 이렇게 풀면 시간 초과가 뜨지 않을까 걱정했는데 일단 시도했고 시간을 확인해보니 괜찮아서 진행했다.


---
# [BOJ] 14503 : 로봇 청소기

### 📌 문제 출처

- [BOJ] 14503 : 로봇 청소기
- [문제 출처 링크로 이동](https://www.acmicpc.net/problem/14503)


### ❓예제입력

```text
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
```

### ‼️접근 방식

- 맵이 나오면 방문 정보를 어떻게 처리할 것인지 파악해야 한다.
    - 방문 정보를 처리하는 방식은 방문 정보만 담을 것인지, 추가적인 정보까지 담을 것인지 두 가지로 분류된다.
        - 방문 정보만 담을 경우 : 맵 크기와 같은 별도의 리스트를 초기화 한다.
        - 방문 정보 이상의 정보를 담을 경우 : 맵 정보에 방문 정보를 추가해서 사용, 별도 리스트 X
            - 방문 정보뿐만 아니라 추가적인 데이터를 표시할 경우 이렇게 표시한다.
    - 현재 주어진 맵에서는 방문 정보를 별도의 리스트로 관리하는 것이 좋다.
- 맵의 상태 파악하기
    - 첫 번째 칸이 (1,1)인지 (0,0)인지
    - 해당 문제는 (0,0) 으로 들어와서 일반적인 행렬로 생각하면 칸이 하나씩 밀림!

### 🔎 알고리즘 및 코드 구현

```python
# 로봇 청소기
# 22.10.3
# 구현

n, m = map(int, input().split())
d = [[0]*m for _ in range(n)]
x, y, direction = map(int, input().split())
d[x][y] = 1
data = [list(map(int,input().split())) for _ in range(n)]
cnt = 1

# 이동 세팅
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    if direction == 0:
        direction = 3
        return
    direction -= 1

def solve(data,x,y):
    global cnt
    turn_time = 0
    while True:
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 벽이 아니고 청소안한 것
        if data[nx][ny] == 0 and d[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            cnt +=1
            turn_time = 0
        # 벽이 아니고 청소한 것
        else:
            # print('벽이 아니고 청소한 것')
            # print('벽이고 청소한 것')
            # print('벽이고 청소 안 한 것')
            turn_time +=1
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            if data[nx][ny] == 0:
                x = nx
                y = ny
                turn_time = 0
            else:
                break
    print(cnt)
solve(data,x,y)
```

### 🕰 시간분석

- 해당 코드의 시간
- 판단한 이유

### ✔️ 예외처리

### ⚔️ 코드 스니펫 및 내장 모듈

```python
# 코드 스니펫

# 띄어쓰기 구분된 문자 => 개별 문자
n, m = map(int, input().split()) 
# 행구분으로 반복되어 들어오는 띄어쓰기 구분된 문자 => 리스트 , list comprehension
data = [list(map(int,input().split())) for _ in range(n)] 

# 방문 정보 파악 위해 초기화
d = [[0]*m for _ in range(n)]

# 이동 정보 파악
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 회전
def turn_left():
    global direction
    if direction == 0:
        direction = 3
        return
    direction -= 1
```

```python
# 내장 모듈
```

### ☑︎ 회고

> 맵의 정보를 받을 때 (0,0) 을 (1,1)로 착각해서 헤맸다. 모든 경우에서 print()를 찍어서 확인해 잘못된 부분을 찾을 수 있었다. 접근 방식에 추가적으로 써뒀는데 이 부분을 까먹지 말고 확인해야할 것 같다. 또 turn_time 의 위치를 잘못 놔둬서 무한루프가 돌았는데, 이를 해결하기 위해 모든 코드를 다 수정하게 되었다. 코드 상으로는 한 줄의 실수 였지만, 의미적으로 큰 실수라는 것을 느꼈다.

---

# [BOJ] 2504 : 괄호의 값

### 📌 문제 출처

- [BOJ] 2504 : 괄호의 값
- [문제 링크](https://www.acmicpc.net/problem/2504)

### ❓예제입력

```

```

### ‼️접근 방식

- 아예 접근도 못해서 고민하다 검색함
- 스택 자료구조에 넣고 비교하는 방식으로 해야하는 것 같음
    - 열린 괄호를 만나면 스택에 넣고 닫힌 괄호를 만나면 스택의 TOP 을 꺼내서 비교하는 방식
- 값 계산에 대한 접근 방식
    - 괄호가 열리면 종류에 맞게 값을 곱한다.
    - 닫히고 나면 최종 값에 더해준다.

### 🔎 알고리즘 및 코드 구현

```python
# 괄호의 값
# 22.10.3
# 구현
# 못 품, 블로그 참조

bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)
```

### 🕰 시간분석

- 해당 코드의 시간
    
    일차 시간
    
- 판단한 이유
    
    반복문이 하나라서 일차 시간이라고 판단했고, 입력의 크기가 30밖에 되지 않기 때문에 삼차 시간이 나와도 넉넉하게 감당할 수 있는 수준임. 이 문제는 시간보단 알고리즘과 자료구조가 중요했던 문제라고 생각함. 그래서 꽤 까다로웠던 것 같은데 실버인 것 같음. 
    

### ✔️ 예외처리

### ⚔️ 코드 스니펫 및 내장 모듈

```python
# 코드 스니펫

data = list(input()) # 입력 문자 리스트로 받기

test  
# data = ['t','e','s','t']
```

```python
# 내장 모듈
```

### ☑︎ 회고

> 문자열의 길이가 30밖에 되지 않아서 시간 문제는 크게 없을 것이라 생각하고 들어갔다. 근데 오래 고민해도 도저히 감이 안잡혀서 검색 했는데 스택 자료구조를 이용하면 효율적으로 풀이할 수 있다는 것을 배웠다.
>