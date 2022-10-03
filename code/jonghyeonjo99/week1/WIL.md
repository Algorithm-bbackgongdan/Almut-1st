# 그리디 알고리즘
현재 상황에서 가장 좋은 것만 고르는 방법
- 알고리즘 암기도 중요하지만, 문제를 풀기 위한 창의력을 기르는 것이 더 중요!
- '가장 큰 순서대로' 등의 문제에서 주어지는 힌트 캐치

# 그리디 알고리즘의 정당성
탐욕적인 방법(아이디어)을 찾았을 때, 그 방법이 정당한지 검토해야한다.
- 계속해서 자신의 아이디어를 발전시켜나가는 것이 중요.
- 그 과정에서 정당성 검토 필수!

# 1541 : 잃어버린 괄호
## code
```python
a = input().split('-') # -를 기준으로 나누기
res = []
for i in a:
  sum = 0
  b = i.split('+') # 더할 숫자들
  for j in b:
    sum += int(j)
  res.append(sum)
  
num = res[0]
for i in range(1,len(res)):
  num -= res[i]
print(num)
```
### 결과
성공
### 접근
처음에는 연산자가 나오면 연산자 앞 뒤의 정수를 괄호로 묶어 먼저 계산하는 방식을
생각했었는데, 

상당히 비효율적이라는 판단에 생각을 접었다.

그 이후, '-'연산자를 기준으로 정수를 묶어 모든 수를 빼주었을 때 최솟값이 나온다는 생각을 하였다.

먼저 '-'연산자를 기준으로 문자열을 파싱 후, 파싱된 문자열에 '+'연산자가 있으면 모두 더해주었다.

결과값들을 배열에 저장 후, 모든 값을 빼서 최솟값을 만들 수 있었다.
## 문제 회고
'-'연산자로 묶는 생각에 도달하기까지 시간이 시간이 조금 오래걸렸다.
# 1461 : 도서관
### code
```python
import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
place = list(map(int,input().split()))

num1 = [0] #음수
num2 = [0] #양수

for i in range(n):
  if place[i] < 0:
    num1.append(place[i])
  else:
    num2.append(place[i])

num1.sort()
num2.sort(reverse=True)

com = -num1[0] #절대값 비교를 위해

if com > num2[0]: #음수 절대값이 더 클 때
  res = 0
  for i in range(m,len(num1),m):
    num = -num1[i]
    res += num * 2
  for j in range(0,len(num2),m):
    res += num2[j] * 2
  res += com
  print(res)

else:
  res = 0
  for i in range(0,len(num1),m):
    num = -num1[i]
    res += num * 2
  for j in range(m,len(num2),m):
    res += num2[j] * 2
  res += num2[0]
  print(res)
  ```
### 결과
성공
### 접근
예시문제들을 살펴보고 음수와 양수에 위치해있는 책은 동시에 놓을 수 없는 것을 깨달았다.

그래서 음수와 양수를 따로 분리하고, 절대값이 가장 큰 위치에 놓아야하는 책은 편도로 이동해야함을 깨달았다.

최소로 이동해야하기 때문에 음수는 오름차순으로, 양수는 내림차순으로 정렬해야했다.
## 문제 회고
예시문제를 통해서 문제 해결 방향을 빠르게 찾을 수 있었다.
# 2138 : 전구와 스위치
### code
### 결과
실패
## 문제회고
스위치를 어떤 규칙을 가지고 끄고 켜야 최소횟수가 나오는지 생각해내지 못했다.