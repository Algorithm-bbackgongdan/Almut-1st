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
