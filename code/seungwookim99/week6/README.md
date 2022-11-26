# Week 6

6주차에 대한 WIL

# 11053 : 가장 긴 증가하는 부분 수열

## 😎 Solved Code

### 💻 Code

```python
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
DP = [0] * N
for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            DP[i] = max(DP[i], DP[j])
    DP[i] += 1

print(max(DP))
```

### ❗️ 결과

성공

### 💡 접근

주어진 수열 A에 대해 DP 리스트를 만들어, A[0:i+1] 의 가장 긴 증가하는 부분 수열의 길이를 DP[i]에 담았다.

따라서 DP를 0부터 n까지 bottom-up 방식으로 순회하며 구했다. 0 ~ i-1 까지 A의 원소를 살펴본 결과 i번째 원소보다 작을 경우 `max(DP[i], DP[j])` 로 DP[i]를 업데이트 했다.

## 🥳 문제 회고

간단한 DP 문제였던 것 같다.

# 1106 : 호텔

## 😎 Solved Code

### 💻 Code1

```python
import sys

C, N = map(int, sys.stdin.readline().rstrip().split())
cities = [
    tuple(map(int,
              sys.stdin.readline().rstrip().split())) for _ in range(N)
]
cities = sorted(cities, key=lambda x: (x[0], x[1]))
INF = int(1e9)
DP = [INF] * (C + 101)
DP[0] = 0

for i in range(N):
    cost, benefit = cities[i]
    for j in range(benefit, C + 101):
        DP[j] = min(DP[j - benefit] + cost, DP[j])

print(min(DP[C:]))
```

### 💻 Code2

```python
import sys

C, N = map(int, sys.stdin.readline().rstrip().split())
cities = [
    tuple(map(int,
              sys.stdin.readline().rstrip().split())) for _ in range(N)
]
cities = sorted(cities, key=lambda x: (-(x[1] / x[0]), x[0]))

INF = int(1e9)
DP = [INF] * (C + 101)
DP[0] = 0

for i in range(N):
    cost, benefit = cities[i]
    for j in range(benefit, C + 101):
        if DP[j] > DP[j - benefit] + cost:
            for k in range(benefit + 1):
                DP[j - benefit + k] = min(DP[j - benefit] + cost, DP[j - benefit + k])
print(DP[C])
```

### ❗️ 결과

성공 - code1은 일부 구글링

### 💡 접근

### Code 1

DP를 이용해 memoization 기법으로 cost list를 중간 저장하고, 이를 불러와서 cost list(위 코드에서 DP 리스트)를 업데이트 하는 방식으로 해결해야겠다고 생각했다. 근데 막상 떠올리려 하니 상당히 어려웠다.

그럼에도 한가지 규칙을 정하고 문제에 접근해보고자 했다.

- 어떠한 기준으로 `도시를 홍보할 때 드는 비용, 얻을 수 있는 고객`을 정렬한다. 이는 cities에 튜플리스트로 저장했다.
- 도시를 순회하며 DP list 전체를 업데이트 해 나간다.

정렬은 `비용에 대한 오름차순` 으로 했다. 아무래도 비용이 적은 것 부터 먼저 채워나가는 것이 그리디 알고리즘 측면에서 정답에 빠르게 다가갈 수 있다고 생각했다. (나중에 알게 된 것인데 어차피 결국 모든 도시를 순회하며 DP list를 최적의 상태로 업데이트 하기 때문에, 도시를 정렬하는것은 의미가 없어보이기도 하다… 확실하지는 않지만 정렬 기준을 바꿔도 정답이 나왔다)

그럼 cities에 대해 하나씩 순회를 하며 DP 리스트를 업데이트 한다.

`DP[j] = min(DP[j - benefit] + cost, DP[j])` 을 보면 기존의 DP[j]와 DP[j - benefit] + cost 를 비교해 최솟값으로 업데이트 한다. benefit은 얻을 수 있는 고객 수 인데, j - benefit 명의 최소 비용에 cost를 더하면 j명에 대한 새로운 비용이 나오고, 이는 기존의 DP[j]보다 작을 가능성이 있기 떄문이다. 이런 방식으로 모든 city에 대해 업데이트를 해준다.

최종 답은 `min(DP[C:])` 으로 구했다. 최솟값이 C 이상에서 나올 수 있기 떄문이다.

최종 답을 도출하는 과정을 구글링 했는데,, 사실 와닿지가 않았다. 문제를 풀며 비슷하게 접근했지만, 매 iteration마다 항상 최적의 cost를 담고 있지 않기 때문에 마지막에 min(DP[C:]) 로 문제를 해결한 것 같았다. 사실 `C명 이상의 cost중에서 반드시 정답이 나오는지` 납득이 안됐다. 반례가 있지 않을까 생각도 들었고 이해도 잘 안되고 찝찝해서 내 식대로 다시 풀어봤다.

### Code 2

code 1 과 비슷하게 접근했지만, cities를 순회하는 iteration이 끝날 때 마다 항상 최소의 비용을 저장하고 있게 했다. 바꾼 부분은 아래와 같다.

```python
 for j in range(benefit, C + 101):
        if DP[j] > DP[j - benefit] + cost:
            for k in range(benefit + 1):
                DP[j - benefit + k] = min(DP[j - benefit] + cost, DP[j - benefit + k])
```

만약 DP[j] > DP[j - benefit] + cost 라면 code 1 에서는 `DP[j] = min(DP[j - benefit] + cost, DP[j])` 으로 DP[j]만 업데이트 했다. 하지만 실제로는 DP[j - benefit] 부터 DP[j] 까지 비용이 최적화 될 수 있다. 예를 들어 아래와 같은 상황이다.

```python
# 현재 DP
DP = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 ...]

# 다음 iteration
cost, benefit = 3, 5

# DP[j - benefit] = DP[5 - 5] = 0
# DP[j] = DP[5] = 5
즉, DP[j] == 5 > DP[j - benefit] + cost == 3
DP[0], DP[1], DP[2], ... DP[5] 중 DP[4], DP[5]가 cost == 3 으로 최적화 될 수 있다.

# for k in range(benefit + 1) 처리 이후
DP = [0,1,2,3,3,3,4,...]
```

위와 같이 매 iteration 마다 항상 최적의 cost를 저장하면 마지막에 정답 출력시에 DP[C]를 출력하면 된다.

시간복잡도는 O(N*C*benefit의 최댓값) 이고 N*C*benefit 최댓값 = 20 _ 1000 _ 100 = 200만 으로 제한된 시간 안에 해결이 가능하다.

## 🥳 문제 회고

DP가 정말 어려운 것 같다… 특히나 비중이 높고 중요한 주제인 만큼 많은 연습이 필요해 보인다.
