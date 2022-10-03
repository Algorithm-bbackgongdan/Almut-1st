# Week 1

## 1. [BOJ 1541] 잃어버린 괄호

### 1️⃣ 구현 코드
```python
data = list(input().split('-'))
def solve(data):
    minus = 0
    ans = 0
    if '+' in data[0]:
        data[0] = sum(list(map(int, data[0].split('+'))))
        ans = data[0]
    else:
        data[0] = int(data[0])
        ans = data[0]
    for i in range(1,len(data)):
        data[i] = list(map(int,data[i].split('+')))
        data[i] = sum(data[i])
        minus += data[i]
    ans -=  minus
    return ans
print(solve(data))
```

### 2️⃣ 접근 방식
'-' 가 나온 뒤의 값을 모두 더해서 크게 만들어 주면 문제에서 요구하는 형태가 나온다.
이 부분을 확인하고 나머지 예외 처리를 구현해줬다.

### 3️⃣ 회고
예전에 풀어본 적 있는 것 같아서 금방 풀었는데 뭔가 코드가 깔끔하진 않다.

---

## 2. [BOJ 1461] 도서관

### 코드
```python

# 데이터 입력
n, m = map(int, input().split())
data = list(map(int, input().split()))
first = [] # 가장 큰 값이 존재하는 리스트
second = [] # 큰 값이 없는 리스트
# 데이터 전처리
for val in data:
    if val > 0:
        first.append(val)
    else:
        second.append(abs(val))
first.sort(reverse=True)
second.sort(reverse=True)

# print('first',first)
# print('second',second)

# 알고리즘 적용
def solve(first,second):
    test = []
    for val in range(0,len(first),m):
        test.append(first[val])
    for val in range(0,len(second),m):
        test.append(second[val])
    ans = max(test)
    test.remove(max(test))
    ans += sum(test)*2
    print(ans)
solve(first,second)
```

### 접근 방식
- 0에서 계속 가까운 것만 더한다?
  - 반례 : (-6,2,7)
- M 개를 선택할 때 0에서 가장 가까운 양수, 음수 각각 M 개씩 선택한다.
  - 반례 : 예제 입력 1
- 예제 분석
  - 예제 분석을 통해서 규칙을 찾아냈고 다음과 같이 알고리즘을 생각해냈다.
    - ```python
      # 7 2
      # -37 2 -6 -39 -29 11 -28
      a = [39, 37, 29, 28, 6]
      b = [2, 11]
      # (11 + 6 + 29 ) * 2 + 39 = 131
      ```
    - ```python
      # 8 3
      # -18 -9 -4 50 22 -26 40 -45
      a = [45, 26, 18, 9, 4]
      b = [50, 40, 22]
      # ( 9 + 45 ) * 2 + 50 = 158       
      ```

### 알고리즘
- 데이터 전처리
  - 음수와 양수를 분리 시키고 절대값 처리
  - 내림차순 정렬
- m 값과 리스트의 길이에 대한 분석
  - 0, m, 2*m, 3*m, len(list) 의 인덱스를 통해 값 추출
  - 답 : 가장 큰 값 + (가장 큰 값 제외한 값의 합 * 2)

### 구현코드

```python
n, m = map(int, input().split())
data = list(map(int, input().split()))
first = [] 
second = [] 
# 데이터 전처리
for val in data:
    if val > 0:
        first.append(val)
    else:
        second.append(abs(val))
first.sort(reverse=True)
second.sort(reverse=True)

# print('first',first)
# print('second',second)

# 알고리즘 적용
def solve(first,second):
    test = []
    for val in range(0,len(first),m):
        test.append(first[val])
    for val in range(0,len(second),m):
        test.append(second[val])
    ans = max(test)
    test.remove(max(test))
    ans += sum(test)*2
    print(ans)
solve(first,second)
```

### 회고
문제 접근 방식을 처음에 떠올리지 못했다. 오래 고민하다가 예제를 분석해서 접근 방식을 찾았다.
예제를 분석하고 나니 규칙이 보여서 그대로 구현하는 데에 시간을 썼고 예제 입력은 모두 답을 출력하는데 정답을 제출하니 런타임에러가 나왔다.
문제가 있을 법한 곳을 고쳐서 다시 제출하니 그냥 틀렸다고 나왔다. 그 뒤로 방황을 하다가 
구현 방식을 아예 바꿔 새롭게 코드를 짰다. 알고리즘 자체는 변하지 않았고 구현 상의 실수로 예외 처리가 되지 않았던 것 같다.
- 예제 분석 잘하자
- 예외 처리 신경 쓰자

---

# 3. [BOJ 2138] 전구와 스위치

### 1️⃣ 구현 코드
```python
import copy

n = int(input())
data1 = list(map(int,list(input())))
target = list(map(int,list(input())))
ans = []

def solve(data1):
    case1 = copy.deepcopy(data1)
    case2 = copy.deepcopy(data1)
    cnt1 = 1
    cnt2 = 0
    # 처음 켜
    case1[0] = (case1[0] + 1) % 2
    case1[1] = (case1[1] + 1) % 2
    
    for i in range(1, len(case1)):
        if (case1[i - 1] != target[i - 1]) and i != len(case1) - 1:  # 가운데 경우
            case1[i - 1] = (case1[i - 1] + 1) % 2
            case1[i] = (case1[i] + 1) % 2
            case1[i + 1] = (case1[i + 1] + 1) % 2
            cnt1 += 1
        elif (case1[i - 1] != target[i - 1]) and i == len(case1) - 1:  # 마지막인 경우
            case1[i - 1] = (case1[i - 1] + 1) % 2
            case1[i] = (case1[i] + 1) % 2
            cnt1 += 1
    if case1 == target:
        # print('case1', case1)
        ans.append(cnt1)

    # 처음 안 켜 
    for i in range(1, len(case2)):
        if (case2[i - 1] != target[i - 1]) and i != len(case2) - 1:  # 가운데 경우
            case2[i - 1] = (case2[i - 1] + 1) % 2
            case2[i] = (case2[i] + 1) % 2
            case2[i + 1] = (case2[i + 1] + 1) % 2
            cnt2 += 1
        elif (case2[i - 1] != target[i - 1]) and i == len(case2) - 1:  # 마지막인 경우
            case2[i - 1] = (case2[i - 1] + 1) % 2
            case2[i] = (case2[i] + 1) % 2
            cnt2 += 1
    if case2 == target :
        # print('case2',case2)
        ans.append(cnt2)
    
    # print('ans   :',ans)
solve(data1)
if len(ans)==0:
    print(-1)
else:
    print(min(ans))
```

### 2️⃣ 접근 방식

- 가장 첫 번째 스위치를 켠 상태에서 시작할 것인지, 안 켠 상태에서 시작할 것인지 분기 처리를 한다.
- i 번째를 비교한다면 i+1 번째 스위치를 켜야 한다.
- i+1 번째 스위치가 처음인지, 가운데인지, 마지막인지에 따라 동작이 다르다.


### 3️⃣ 회고
예제 입력을 참고할 것도 없어서 고민하다 구글에 검색해서 아이디어를 참조했다.
처음 켜지는 값에 대해 분기 처리를 한 다음에 비교하면 된다는 아이디어를 참조하여
구현을 해봤다. 겹치는 부분이 많은데 이를 함수로 빼서 간략화 하는 게 좋았을 것 같다.

정답을 제출했을 때 계속 실패가 떠서 당황했다. 입력 예제도 많지 않아서
다양한 케이스를 확인해가며 예외 처리를 해주는 데에 시간을 썼다.
근데 당황스럽게도 타이포때문에 실패한 것이었고, 고쳐서 다시 제출하니 정답..🥲 

