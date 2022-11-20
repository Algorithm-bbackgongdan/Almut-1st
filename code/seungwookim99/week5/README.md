# Week 5
5주차에 대한 WIL

# 16401 : 과자 나눠주기
## 😎 Solved Code

### 💻 Code

```python
import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
L = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 1, max(L)
res = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for l in L:
        count += (l // mid)
    if count >= M:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)
```

### ❗️ 결과

성공

### 💡 접근

탐색 할 수의 범위가 1,000,000 이므로 O(NlogN)으로 해결 가능하다. 나눠줄 과자의 크기는 1 ~ L의 최대값 범위 안에 있기 때문에 start, end 를 1, max(L)로 지정했다.

그리고 이분탐색으로 mid값을 계속 계산해 나가며 문제를 해결했다.

while문을 돌며 한 iteration당 mid를 고정하고 L 전체를 순회한다. mid 크기로 몇 개의 과자를 나눠줄 수 있는지 계산한다. 그리고 이분 탐색에 의해 start, end를 업데이트 한다.

따라서, start, end를 조정하며 이분탐색 하는 데에 O(LogN)이, 한 iteration당 L을 순회하므로 O(N)이 소요되므로 → O(NlogN)의 시간복잡도이다.

## 🥳 문제 회고

이분 탐색 주제에 대해 제대로 학습이 안 된 상태에서는 대충 원리만 이해하고 bisect 같은 라이브러리만 쓰면 될 줄 알았다. 그런데 이번 주차 교재 연습문제나 이번 문제처럼 이분 탐색 원리를 직접 구현하여 푸는 유형도 존재한다는걸 알았다. 익숙하지 않은 만큼 더 연습해야겠다.


# 2470 : 두 용액
## 😎 Solved Code

### 💻 Code

```python
import sys

N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip().split()))
M, P = [], []
for l in L:
    if l > 0:
        P.append(l)
    else:
        M.append(l)
P.sort()
M.sort(reverse=True)

if len(M) == 0:
    res = [P[0], P[1]]
elif len(P) == 0:
    res = [M[0], M[1]]
else:
    S = float('inf')
    i, j = 0, 0
    res = [M[i], P[j]]
    while i < len(M) and j < len(P):
        if abs(M[i] + P[j]) < abs(S):
            S = M[i] + P[j]
            res = [M[i], P[j]]
        if M[i] + P[j] >= 0:
            i += 1
        else:
            j += 1
    if len(P) >= 2 and abs(P[0] + P[1]) < abs(S):
        res = [P[0], P[1]]
    elif len(M) >= 2 and abs(M[0] + M[1]) < abs(S):
        res = [M[1], M[0]]

print(min(res), max(res))
```

### ❗️ 결과

성공

### 💡 접근

투포인터를 이용해 해결했다. 왜 이렇게 접근했는지 아래에서 설명하겠다.

먼저 산성 용액을 P 리스트에 (양수), 알칼리성 용액을 M 리스트에 (음수) 절대값에 대해 오름차순 정렬 했다.

```python
M = [-1, -2, -99]
P = [4, 98]
```

만약 산성(P) 또는 알칼리성(M) 용액만 존재한다면? 각각 절대값으로 정렬되어있기 때문에 `P[0], P[1]` , `M[1], M[0]` 이 답일 것이다. 그렇지 않고 섞여있다면 어떻게 해결할까?

우선 시간제한 1초에 N의 범위가 10만이므로 O(NlogN) 이하로 문제를 해결해야 한다. (이미 P, M 정렬하는 데에 O(NlogN) 사용)

P, M을 각각 index 0부터 순회하는 포인터 i, j를 이용하면 탐색 자체는 O(N)에 해결할 수 있을 것 같다.

P[i], M[j] 를 더해보며 0에 가까운 수를 만들어내는 P[i], M[j] 값을 찾아나가면 될 것이다. 위의 예시를 바탕으로 아래에서 시뮬레이션을 해보자.

```python
# i = 0, j = 0
M[0] + P[0] == (-1) + 4 == 3

# 현재까지 답 : M[0], P[0]
```

이 상황에서 결과가 `양수` 가 나왔으니 절대값이 조금 더 큰 `음수` 를 더해주면 0에 가까워질 가능성이 있다. 따라서 M의 포인터(인덱스) i를 1 증가시켜보자

```python
# i = 1, j = 0
M[1] + P[0] == (-2) + 4 == 2

# 현재까지 답 : M[1], P[0]
```

더 0에 가까워졌다. 하지만 여전히 양수이므로 절대값이 더 큰 음수를 더해주면 0에 가까워질 수 있다. 따라서 또다시 M의 포인터 i를 1 증가시켜보자

```python
# i = 2, j = 0
M[2] + P[0] == (-99) + 4 == -95

# 현재까지 답 : M[1], P[0]
```

이번에는 음수의 절대값이 너무 커서 두 용액의 합이 음수가 되었다. 따라서 현재까지의 답은 변하지 않는다. 다만 이번에는 좀 더 큰 양수를 더하면 0에 가까워질 수 있을 것이다. 따라서 다음 시뮬레이션에는 j를 1 증가시키게 된다.

이렇게 차근차근 i, j 포인터를 증가시키며 가능한 최적의 모든 경우의 수를 O(N)에 탐색하며 0에 가장 가까운 답을 찾아낼 수 있다.

마지막으로 처리할 예외상황이 있다. 지금까지 시뮬레이션은 산성, 알칼리성 용액이 섞여있을 경우 M, P에서 각각 하나씩 선택해 더하며 0에 가까운 수를 구했다. 그러나 오직 산성 또는 알칼리성 용액에서 두 용액을 꺼내 더한 것이 0에 더 가까울 수 있다. 예를 들어 `[-99, 1, 2]` 같은 상황이다. 시뮬레이션대로면 `-99, 1` 을 고를 것이지만 실제 답은 `1,2` 다. 마지막에 해당 예외처리를 해준다.

## 🥳 문제 회고

이분탐색으로 해결할 방법이 떠오르지 않아 투 포인터를 택했다. 0에 가장 가까운 값을 고르기 위한 전략을 취해야 한다는 점에서 `그리디 알고리즘` 을 사용했다고 할 수도 있다. 다만 이를 위해 시간복잡도를 고려해야 했던 문제였다.


# 1561 : 놀이 공원
## 😎 Solved Code

### 💻 Code

```python
import sys

def solve(N, M, L):
    if N <= M:
        print(N)
        return
    MAX_N = 2000000000  # N : 1 ~ 20억
    start, end = 0, 30 * MAX_N  # 탐색 가능한 최대 시간

    # N번째 아이가 탑승 가능한 최소 시간(분) 탐색
    T = 0
    riding = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for l in L:
            cnt += mid // l
            cnt += 1 if mid % l else 0
        if cnt > N:
            end = mid - 1
        else:
            start = mid + 1
            T = mid
            riding = cnt

    # 만약 N번째 아이까지 전부 탑승한 시간 T를 구했다면, N이 탑승 가능한 최소 시간 탐색
    while riding == N:
        T -= 1
        cnt = 0
        for l in L:
            cnt += T // l
            cnt += 1 if T % l else 0
        riding = cnt
    # T분에 몇 번째 놀이기구를 타는지 탐색
    order = N - riding - 1  # 남아있는 사람 중 N이 탈 순서 (0부터 시작)
    rides = []  # 0 ~ order 번까지 몇 번 기구를 타는지 저장
    for i in range(len(L)):
        if T % L[i] == 0:
            rides.append(i + 1)  # 기구의 번호 (i+1) 저장
    print(rides[order])
    return

N, M = map(int, sys.stdin.readline().rstrip().split())
L = list(map(int, sys.stdin.readline().rstrip().split()))
solve(N, M, L)
```

### ❗️ 결과

성공 - 일부 구글링

### 💡 접근

N의 범위가 20억인게 심상치 않다. O(logN)에 해결해야할 것 같은 느낌이 든다.

1 ~ N명을 순차적으로 순회하며 몇 번째 놀이기구에 타는지 구한다 → O(N)이므로 당연히 X

그럼 N명에 대해 이분탐색을 진행해야 할까…? N번째 아이가 몇 번째 놀이기구를 타는지 구하는 문제인데 뭔가 잘못된 접근 같다.

일단 여기에서 막혀서 고민하다 구글에서 힌트를 얻었다.

바로 `경과 시간` 을 이분탐색 하는 문제로 바꿔 푸는 것 이었다. T분에 지금까지 몇 명의 아이들이 탑승했는지 구하는 것은 생각보다 간단하다. 아래와 같이 O(M)에 구할 수 있다. (M은 범위가 10000 이다)

```python
for l in L: # L은 놀이기구
		cnt += T // l
    cnt += 1 if T % l else 0
```

그럼 N번째 아이가 탈 수 있는 최소 시간 T를 구하면 문제를 해결할 수 있다.

T의 범위를 `0 ~ 20억 * 30` 으로 잡고 이분 탐색을 진행하면 될 것이다. `20억 * 30` 이라는 수는 놀이기구가 한 개(M==1)이고, 운행 시간이 30분, N = 20억 일 때 상황으로 가장 극한의 상황이다.

이분탐색을 진행하며 T분 직전까지 탑승한 아이들의 수를 구하고, N보다 큰 지 작은 지를 기준으로 start, end 값을 조정해 나아가면 된다.

## 🥳 문제 회고

도저히 생각이 안났다. 수의 범위를 보고 당연히 이분탐색을 사용해야겠다 생각했지만, 탐색의 대상을 선정하는 것 부터 고민이 많았다. 구글링을 해서 이분탐색의 대상을 `시간` 으로 정하는 힌트를 얻었다. T분이 지났을 때 `몇 명이 타고 있는가` 를 구하는게 핵심이었던 것이다. 이분탐색을 이렇게 활용할 수 있는게 신기하기도 하고,,, 너무 어려웠다