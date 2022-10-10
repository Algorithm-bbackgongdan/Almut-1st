# 2504 : 괄호의 값
## code
```python
stack = [] 
temp = 1 
result = 0 
a = list(input()) 


for i in range(len(a)):
  if a[i]=='(':
    temp *= 2
    stack.append(a[i])
    
  elif a[i]=='[':
    temp *= 3
    stack.append(a[i])
    
  elif a[i]==')':
    if not stack or stack[-1]!='(':
      result = 0
      break
    if a[i-1]=='(': result += temp
    temp //= 2
    stack.pop()
    
  elif a[i]==']':
    if not stack or stack[-1]!='[':
      result = 0
      break
    if a[i-1]=='[': result += temp
    temp //= 3
    stack.pop()

if stack:
  print(0)
else:
  print(result)
  
  # 괄호 쌍이 맞지않는 케이스를 stack으로 구현
```
### 결과
성공
### 접근
- 처음에 괄호의 짝의 개수가 맞지않으면 0을 출력하는 방법으로 구현하였다. (40% 실패) 반례) "([)]"
- 자료구조 스택을 이용하여 괄호의 짝이 맞는지 여부까지 확인해주었다.
## 문제 회고
여름방학 중 교내 동아리에서 풀었던 기억이 있던 문제였다.
당시에 굉장히 어려워 풀지 못하였는데, 동아리 운영진 분들의 풀이를 학습했던 기억이 있어 그대로 풀었다.
# 14503 : 로봇청소기
### code
```python
n,m = map(int,input().split())
x,y,d = map(int,input().split())
arr = []
for i in range(n):
  arr.append(list(map(int,input().split())))

dx = [0, -1, 0, 1] 
dy = [-1, 0, 1, 0]

arr[x][y] = 1 #시작위치 카운트
cnt = 1

while (True):
  flag = 0
  for i in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    if d == 0:
      d = 3
    elif d == 3:
      d = 2
    elif d == 2:
      d = 1
    elif d == 1:
      d = 0
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
      arr[nx][ny] = 1
      cnt += 1
      flag = 1
      x = nx
      y = ny
      break
  if flag == 0:
    nx = x - dx[d]
    ny = y - dy[d] #후진
    if arr[nx][ny] == 0: #후진할 수 있다.
        x = nx
        y = ny
    else: #후진도 못한다.
        print(cnt)
        break

  ```
### 결과
실패
### 접근
- 문제의 순서대로 청소기가 움직일 수 있도록 코드구현
- 왼쪽으로 회전하여 이동할 때마다 현재의 위치를 기준으로 상대적인 위치 좌표를 리스트에 저장하여 다음 위치를 생각하였다.
## 문제 회고
로봇청소기의 머리방향을 if문을 통해 구현하였는데, 검색을 통해서 d = (d+3) % 4라는 식으로 정리 할 수 있음을 알았다.
코드를 조건에 맞게 쓴거같은데 테스트케이스 출력값이 나오지않아 머리가 많이 아팠다.
# 15686 : 치킨배달
### code
```python
import itertools

n,m = map(int,input().split())
arr = []
num1 = [] # 집 
num2 = [] # 치킨

for i in range(n):
  arr.append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      num1.append(i+1)
      num1.append(j+1)
    elif arr[i][j] == 2:
      num2.append(i+1)
      num2.append(j+1)

num1_index = [num1[i*2:(i+1)*2] for i in range((len(num1)+1)//2)] #집 좌표
num2_index = [num2[i*2:(i+1)*2] for i in range((len(num2)+1)//2)] #치킨 좌표

com = list(itertools.combinations((num2_index),m)) #치킨집 m개 조합

num = 0
for i in range(len(num1_index)):
  minimal = []
  for j in range(0,m):
    list =[]
    temp = abs(num1_index[i][0] - com[i][j][0]) + abs(num1_index[i][1] - com[i][j][1])
    list.append(temp)
  res = min(list) #집x와 치킨집 사이의 치킨거리.
  num += res #도시의 치킨거리
  minimal.append(num)
print(min(minimal))
  ```
### 결과
실패
### 접근
- 주어진 도시의 정보에서 집과 치킨집 좌표만 뽑는다.
- x개의 치킨집 중 m개만 남겨야하므로 나올 수 있는 치킨집 조합은 xCm개 이다.
- 치킨집 조합을 만들어두고 각 집에서 치킨집 조합까지 치킨거리를 구한 후 모두 더한다.
- 더해진 값들 중 최소값이 도시의 치킨거리이다.
## 문제회고
xCm개의 치킨집 조합을 만드는데까지는 성공하였으나,
치킨집 조합과 각 집 사이의 도시의 치킨거리를 구하는 코드를 
구현하지 못하였다.

## 이번 스터디를 하면서 느낀 점
---
흔히 구현은 피지컬이 좋아야 잘 푼다고 하는데,
이번 스터디를 통해서 그 말을 실감할 수 있었다.
머리속의 아이디어를 코드로 구현해내기 위해서는 더 큰 노력이 필요할 것같다.

