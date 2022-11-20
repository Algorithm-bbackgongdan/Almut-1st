# 16401 : 과자나눠주기
## code
```python
import sys

m, n = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

# 가장 긴 막대과자 나누기
while m > n:
  temp = arr[n-1] // 2
  arr[n-1] = (arr[n-1] - (temp))
  arr.append(temp)
  arr.sort()
  n += 1

start = 0
end = max(arr)
result = 0
while(start <= end):
  total = 0
  mid = (start + end) // 2
  # 나누어줄 수 없을 때 0 출력
  if mid == 0:
    total = 0
    break

  for x in arr:
    if x >= mid:
      total += mid
  if total < mid * m:
    end = mid - 1
  elif total > mid * m:
    start = mid + 1
  else:
    result = mid
    start = mid + 1
print(result)
```
### 결과
실패
### 접근
우선 조카의 수만큼의 막개과자가 필요하다고 생각해서 조카의 수보다 막대과자의 개수가 적을 경우, 조카의 수와 막대과자의 수가 같아질 때까지 가장 긴 막대과자를 절반으로 나누어주었다.

그 다음 가장 긴 막대를 기준으로 mid를 설정하여 mid의 길이보다 긴 막대들을 잘라 모든 막대과자의 길이가 mid*(조카의 수)가 될 때까지 이진탐색을 해주었다.

## 문제 회고
위의 접근으로 풀었을 때, 테스트케이스는 모두 잘 나오는데 오답처리가 된다. 오답인 이유를 찾지못했다. 피드백 부탁드립니다ㅠ
그리고 다시 처음부터 풀어보았다.

## code
```python
import sys

m, n = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

arr.sort()

start = 0
end = max(arr)
result = 0
while(start <= end):
  total = 0
  mid = (start + end) // 2
  if mid == 0:
    total = 0
    break

  for x in arr:
    if x >= mid:
      total += (x//mid)
  if total >= m:
    start = mid + 1
    result = mid
  else:
    end = mid - 1
print(result)
```
### 결과
성공
### 접근
위에서는 조카들에게 나누어줄 수 있는 가장 긴 막대과자 길이를 기준으로 구현했는데, 이번에는 mid길이만큼 막대과자를 잘랐을 때 생성되는 막대과자의 개수를 기준으로 구현해보았다.

mid길이의 막대과자의 개수가 조카의 수보다 많거나 같을 때 가장 긴 막대과자를 선택하고자 하였다.

## 문제 회고
처음 코드보다 간결하게 작성되었는데, 가장 길이가 긴 막대과자에서 조카들에게 나누어줄 수 있는 과자가 2개이상 만들어질 수 있다는 생각을 하기까지 시간이 오래걸렸다.

# 2470 : 두 용액
### code
```python
n = int(input())
arr = list(map(int,input().split()))

arr.sort()

start = 0
end = n-1
result = abs(arr[start] + arr[end])
left = start
right = end
while (start < end):
  temp = arr[start] + arr[end]
  if abs(temp) < result:
    result = abs(temp)
    left = start
    right = end
    if result == 0:
      break
  elif temp > 0:
    end -= 1
  elif temp < 0:
    start += 1

print(arr[left],arr[right])
```
### 결과
성공
### 접근
start와 end가 정렬된 배열의 양쪽 끝에서부터 탐색을 시작하여
두 수의 합이 0이 되는 값을 찾고자 하였다.
같은 수를 더하면 안되기 때문에 이진탐색 while문의 조건을 "start < end"로 설정하였다.

배열의 양쪽 끝에 있는 값사이의 절대값 합을 result에 저장한 후
result값과 abs(temp)값을 비교하였다. result보다 temp의 절대값이 작으면 result값을 갱신해주고, 두 수의 합이 0에 가까워지기 위해서 temp값이 양수이면 end값을 왼쪽으로 이동시켜주고, 음수이면 start값을 오른쪽으로 이동시켜주면서 탐색하였다.

## 문제 회고
값을 하나하나 비교해가면서 정답을 찾는 느낌이 들어 시간초과가 나지 않을까 걱정했지만 다행히 정답처리가 되었다.

mid값을 쓰지않고, start와 end를 사용하는 투 포인터 알고리즘을 배울 수 있었다.

# 1561 : 놀이공원
놀이공원 문제는 현재 고민 중에 있습니다.ㅠㅠ
### code
```python

```
### 결과

### 접근

## 문제회고


