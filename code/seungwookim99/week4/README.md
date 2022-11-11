# Week 4
4주차에 대한 WIL

# 1931 : 히의실 배정
## 😎 Solved Code

### 💻 Code

```python
import sys

START, END = 0, 1

N = int(sys.stdin.readline().rstrip())
Times = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    Times.append((s, e))

Times = sorted(Times, key=lambda x: (x[1], x[0]))  # 종료시간으로 정렬
count = 1
end = Times[0][END]
for i in range(1, N):
    if Times[i][START] >= end:
        count += 1
        end = Times[i][END]
    else:
        continue

print(count)
```

### ❗️ 결과

성공

### 💡 접근

어떻게 해야 최대한 많은 강의실을 배정할 수 있을까? 분명 어떤 특정한 규칙에 의해 강의실을 선택해야 할 것이다. 뭔가 가능하다고 생각하는 방법들을 하나씩 검토해보자.

1. 시작 시간이 가장 짧은 강의 먼저 선택
    - 아무리 시작 시간이 짧아도 종료 시간이 긴 경우가 있다. 예외 사항 발견으로 PASS
2. 강의 길이가 가장 짧은 순서대로
    - 만약 길이 4짜리 강의들 (0,4) (4,8) (8,12) 과 길이 2짜리 강의들 (3,5) (7,9) 가 있다고 하자. 그럼 길이 2 강의 두 개를 선택하는데 이는 답이 아니다. 예외 사항 발견으로 PASS
3. 종료 시간이 가장 짧은 강의 먼저 선택
    - 몇몇 테스트 케이스들을 넣어서 해보니 딱히 예외사항이 보이지 않는다.
    - 그리고 직관적으로도 종료시간이 빨라야 바로 이어서 다른 강의들을 더 많이 추가할 수 있을 것 같다.

3번의 아이디어 대로 구현해본다. sorted를 써서 종료시간에 대해 오름차순 정렬한 뒤, 차례대로 순회하며 답을 구한다.

그런데 채점하면 오답이다.

조건 하나를 놓쳤는데, 회의의 시작시간과 끝나는 시간이 같을 수도 있다.

예를 들어 (8,10), (10,10) 두 강의는 종료시간이 같다. 그런데, (10,10)을 먼저 골라버리면 (8,10)을 선택할 수 없다. 따라서 정렬시에 `종료 시간` 에 대해 정렬하고, `시작 시간` 에 대해서도 정렬을 해야 한다.

`sorted(Times, key=lambda x: (x[1], x[0]))` 으로 조건에 맞게 정렬했다.

## 🥳 문제 회고

전에 학교에서 알고리즘 수업을 들을 때 중요하게 다뤘던 문제라 금방 기억이 났다. 그런데도 문제 제대로 안읽어서 헤맸다,,, 문제를 꼼꼼히 읽어야겠다.


# 1202 : 보석 도둑
## 🥺 Unsolved Code

### 💻 Code

```python
import sys
import heapq
from bisect import bisect_left

N, K = map(int, sys.stdin.readline().rstrip().split())
Jew = []
for _ in range(N):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    heapq.heappush(Jew, (-v, m))
Bag = [int(sys.stdin.readline().rstrip()) for _ in range(K)]
Bag = sorted(Bag)

res = 0
while Jew and Bag:
    v, m = heapq.heappop(Jew)
    idx = bisect_left(Bag, m)
    if idx == len(Bag):  # 못담음
        continue
    res += abs(v)
    del Bag[idx]

print(res)
```

### ❗️ 결과

실패 - 시간 초과

### 💡 접근

보자마자 그리디 알고리즘이란 생각이 들었다. 그럼 어떤 기준으로 그리디를 생각해야할까?

당연하게도 가장 큰 가격의 보석을 우선적으로 담아야 할 것이다.

그럼 보석 가격에 대해 정렬 또는 max heap을 만들면, 보석 무게는 랜덤한 순서로 주어질 것이다.

보석 가격에 대한 max heap을 만들고, 해당 보석을 어느 가방으로 담을 수 있을지만 판단하면 될 것 같다.

heapq를 이용해 보석들을 보석 가격에 대해 max heap으로 저장했다

```python
heapq.heappush(Jew, (-v, m))
```

heapq는 기본적으로 min heap을 만들기 때문에, max heap을 만들려면 음수로 넣어주면 된다.

그리고 Jew(보석)를 하나씩 pop 하며 해당 보석을 어느 가방으로 담을 수 있는지 알아본다. 이를 위해 먼저 가방을 무게에 대해 오름차순 정렬했다. 그리고 `bisect_left(Bag, m)` 을 이용해 보석을 담을 수 있는 가능한 가장 작은 용량의 가방을 찾는다. 이는 시간복잡도 O(logN) 이다. 마지막으로 담은 가방을 del Bag[idx] 으로 제거한다.

여기에서 놓친 점이 있었다.

del Bag[idx] 는 O(N)이기 때문에, 결국 이 알고리즘은 O(N^2)의 시간복잡도가 소요된다.

정리해보면 Jew를 순회하며 O(N)이 소요되는데, 그 내부에서

1. 가능한 가방 탐색 : O(logN)
2. 가방 제거 (사용한 가방 빼기) : O(N)

위 두 가지 연산을 수행하므로, 최종적으로 O(N * (logN + N)) ⇒ O(N^2) 인 것이다.

당연하게도 시간 초과로 펑.

### 🧐 접근에 대한 회고

가장 큰 값을 담아야 한다는 기본 아이디어는 변함이 없다. 하지만 접근을 달리 해야할 것 같다.

머리를 비우고 처음부터 다시 짜봤다.

## 😎 Solved Code

### 💻 Code

```python
import sys
import heapq
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
Jew = []
for _ in range(N):
    m, v = map(int, sys.stdin.readline().rstrip().split())
    Jew.append((m, v))
Bag = deque(int(sys.stdin.readline().rstrip()) for _ in range(K))
Bag = sorted(Bag) # 가방 용량으로 정렬
Jew = sorted(Jew, key=lambda x: (x[0])) # 보석 무게로 정렬

candidate = []

res = 0
b_i, j_i = 0, 0 # 가방, 보석을 순회하는 인덱스
while b_i < K and j_i < N:
    b = Bag[b_i] # 현재 가방
    while j_i < N and b >= Jew[j_i][0]:
				# 현재 가방으로 담을 수 있는 보석들을 전부 heap에 push
        heapq.heappush(candidate, -Jew[j_i][1]) # 가격에 대한 Max heap
        j_i += 1
    if j_i >= N: # 모든 보석을 순회했다면
        while candidate and b_i < K: # 남은 가방들에 대해 보석을 전부 담음
            res += abs(heapq.heappop(candidate)) # 가장 큰 값의 보석 담음
            b_i += 1
        break
    if candidate:
        res += abs(heapq.heappop(candidate)) # 가장 큰 값의 보석 담음
    b_i += 1 # 다음 가방

print(res)
```

### ❗️ 결과

성공

### 💡 접근

가방을 용량에 대해 정렬, 보석을 무게에 대해 정렬 하고 시작한다.
기본적으로 가방을 기준으로 순회하며, 현재 가방이 담을 수 있는 보석들을 탐색한다. 둘 다 무게(용량)에 대해 정렬이 되어있기 때문에 투 포인터를 이용해 순차적으로 순회하면 된다.

예를 들어 0번째 가방 용량이 3 이고, 보석 무게가 1, 2, 3, 4, 5 로 정렬되어있다고 하자. 그럼 O(N)으로 보석을 순회하며 [1,2,3]이 가능하다는 것을 발견한다. 그럼 이 중에서 가장 가격이 비싼 보석을 담아야 하는데 어떻게 알까?

여기에서 max heap을 사용한다. 보석을 순회하며 매 번 candidate에 가격에 대해 max heap push를 한다 (O(logN)).

위의 예시로 보면 [1,2,3]이 가격에 대한 max heap으로 저장되어있다. 여기에서 가장 큰 값의 보석은 heappop()으로 O(1)에 구하고, 내부적으로 heap 조정을 위해 O(logN)의 시간복잡도가 소요된다.

이런식으로 투 포인터를 이동시키며 candidate에 항상 `지금까지 순회한 모든 담을 수 있는 보석들을 가격에 대한 max-heap` 형태로 저장해 나간다.

시간복잡도는 O(K*logN + N*logN + logN) ⇒ O(N*logN) 이다.

## 🥳 문제 회고

조건이 많아서 상당히 어려웠다. heap을 써야만 해결할 수 있었던 문제인 것 같다.