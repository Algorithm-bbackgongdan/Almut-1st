# Week 1
1주차에 대한 WIL

# 1541 : 잃어버린 괄호
## 😎 Solved Code

### 💻 Code

```python
import sys

s = sys.stdin.readline().rstrip()
if '-' not in s:
    print(sum(list(map(int, s.split('+')))))
else:
    nums = s.split('-', 1)
    front = sum(
        list(map(int, nums[0].replace('+', ' ').replace('-', ' ').split(' '))))
    back = sum(
        list(map(int, nums[1].replace('+', ' ').replace('-', ' ').split(' '))))
    print(front - back)
```

### ❗️ 결과

성공

### 💡 접근

‘-’(마이너스)가 최초로 등장한 이후로는 괄호를 이용해 그 뒤에 등장하는 모든 부호를 바꿀 수 있다는 것을 발견했다.

문제 목표는 가능한 값을 가장 작게 만드는 것이므로, A - B 형태로 식을 정리해 A는 최대한 작게, B는 최대한 크게 만들면 된다.

‘-’ 가 없을 때는 전부 더한 값을 리턴한다.

‘-’가 있을 때는 ‘-’를 기준으로 1회만 나눈다. A - B 형태로 만들기 위함이다 (front - back).

문자열 파싱을 위해 +,- 를 ‘ ‘(공백)으로 바꾼 후 ‘ ‘을 기준으로 나누어 더했다.

## 🥳 문제 회고

마이너스 뒤에 오는 수를 최대한 크게 만들어야 하는 그리디 문제였다. 풀이법을 생각하고 구현하기 까지 큰 어려움은 없었다.


# 1461 : 도서관
## 😎 Solved Code

### 💻 Code

```python
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
books = list(map(int, sys.stdin.readline().rstrip().split()))
cost = 0
books.sort()
m = [0]  # 음수 list
p = [0]  # 양수 list

def add_cost_and_pop(cost, arr, M, isFirst):
    cost += arr[-1] if isFirst else 2 * arr[-1]
    if len(arr) >= M:
        for _ in range(M):
            arr.pop()
    else:
        arr = []
    return cost, arr

for b in books:
    if b < 0:
        m.append(-b)
    else:
        p.append(b)
m.sort()

isFirst = True
while m and p:
    if m[-1] > p[-1]:
        cost, m = add_cost_and_pop(cost, m, M, isFirst)
    else:
        cost, p = add_cost_and_pop(cost, p, M, isFirst)
    isFirst = False

while m:
    cost, m = add_cost_and_pop(cost, m, M, isFirst)

while p:
    cost, p = add_cost_and_pop(cost, p, M, isFirst)
print(cost)
```

### ❗️ 결과

성공

### 💡 접근

출발점(0번 좌표)에서 시작하는 것이 아닌, 이동이 끝났을 시점에서부터 거꾸로 생각해 보았다.

즉, 책꽂이에 있는 책을 출발점으로 전부 들고 오는 문제로 바꿔 생각했다.

대부분 책을 가져다 놓고 돌아오기 때문에 `2 * 책까지의 거리` 만큼 이동해야 한다. 하지만 문제 조건대로 마지막 책을 놓고 출발점으로 돌아오지 않아도 되기 때문에 편도로 움직인다. 그렇다면 `편도로 이동하는 거리`는 `가장 멀리 떨어진 책의 위치`일 것이다.

편도 이동이 끝나면 출발점에 도착할 것이다. 이 때부터는 남은 책들을 왕복으로 가져와야 한다.

좌 우 방향 중(좌표상으로 - 또는 + 방향) 출발점으로부터 가장 거리가 먼 책이 있는 방향으로 먼저 이동하면 된다.

구현은 m, p이라는 리스트를 만들어 각각 좌 우 방향의 거리를 담았다. 그리고 리스트가 빌 때까지 M개만큼 pop을 하며 움직인 거리를 더했다.

## 🥳 문제 회고

주어진 예제에서 어떻게 움직여야 답이 나오는지 고민하는 시간이 길었다. 다행히 예제가 많아 금방 해결을 위한 아이디어를 떠올릴 수 있었다.


# 2138 : 전구와 스위치
## 😎 Solved Code

### 💻 Code

```python
import sys

N_ = int(sys.stdin.readline().rstrip())
orig_ = list(map(int, sys.stdin.readline().rstrip()))
target_ = list(map(int, sys.stdin.readline().rstrip()))

def flip(a):
    return 0 if a else 1

def calc(clickFirst, orig, target, N):
    count = 0
    if clickFirst:
        orig[0] = flip(orig[0])
        orig[1] = flip(orig[1])
        count += 1
    for i in range(1, N - 1):
        if orig[i - 1] == target[i - 1]:
            pass
        else:
            orig[i - 1] = flip(orig[i - 1])
            orig[i] = flip(orig[i])
            orig[i + 1] = flip(orig[i + 1])
            count += 1

    if orig[-1] != target[-1]:
        orig[-1] = flip(orig[-1])
        orig[-2] = flip(orig[-2])
        count += 1

    return count, orig == target

res1_c, res1 = calc(True, orig_.copy(), target_.copy(), N_)
res2_c, res2 = calc(False, orig_.copy(), target_.copy(), N_)

if res1 and res2:
    print(min(res1_c, res2_c))
elif res1:
    print(res1_c)
elif res2:
    print(res2_c)
else:
    print(-1)
```

### ❗️ 결과

성공

### 💡 접근

첫번째와 마지막 스위치는 두 전구만 키기 때문에 특이 케이스다. 따라서 첫번째 또는 마지막을 켜는 여부에 따라 분리했다.

또한 N의 범위가 10만이기 때문에 O(n^2) 이상의 완전탐색을 이용해 풀 수 없을 것이다. 즉, O(n)으로 0번째 인덱스부터 순회하는 방식을 택했다.

calc라는 함수를 만들어 첫번째 스위치를 눌렀는지 여부를 파라미터로 넘겨받아 두가지 답을 도출했다. 

calc 내부에서는 1 ~ N-2 까지 순회하며 만들고자 하는 전구 상태로 만드는 작업을 진행했다. 마지막 전구(N-1)가 다를 경우 마지막 전구를 켠 후, 만들고자 하는 상태와 동일한지 결과를 비교한다.

## 🥳 문제 회고

예외가 상당히 많다고 생각해서 많이 고민했다. 한 함수 안에 모든 분기처리를 하기 까다롭다면, calc를 두 번 호출하는 것과 같이 조금은 단순무식하게(?) 접근해도 좋다.