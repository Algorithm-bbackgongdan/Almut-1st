# 최소힙, 최대힙
- 최소 힙: 루트노드가 가장 작은 값을 가지며, 항상 부모노드는 자식노드보다 작은 값을 갖는다.
```python
def heapsort(iterable):
    heap = []
    result = []
    for value in iterable:
        heapq.heappush(heap, value)
    for i in range(len(heap)):
        result.append(heapq.heappop(heap))
    return result

result = heapsort([1,9,0,7,8,6,3,5])
print(result)
# result
[0, 1, 3, 5, 6, 7, 8, 9] # 오름차순 정렬
  ```
- 최대 힙: 루트노드가 가장 큰 값을 가지며, 항상 부모노드는 자식노드보다 큰 값을 갖는다.

파이썬에서 이를 구현하기 위해 PriorityQueue와 heapq를 사용하는데, heapq가 실행시간이 적게걸려 일반적으로 많이 사용한다.

* 최대힙 구현
  - 파이썬에서는 최대 힙이 구현되지 않기 때문에 내림차순 정렬을 하기 위해서는 모든 원소의 부호에 "-"를 붙여 부호를 바꾼 뒤 최소힙을 이용하여 정렬, 다시 부호를 바꾸는 작업필요.  
  ```python
    def heapsort(iterable):
        heap = []
        result = []
        for value in iterable:
            heapq.heappush(heap, -value)
        # print(heap)
        # [-9, -8, -6, -5, -7, 0, -3, -1]
        for i in range(len(heap)):
            result.append(-heapq.heappop(heap))
        return result

    result = heapsort([1,9,0,7,8,6,3,5])
    print(result)
    # result
    [9, 8, 7, 6, 5, 3, 1, 0] # 내림차순 정렬
  ```


# 1931 : 회의실 배정
## code
```python
  from sys import stdin

meeting = []
res = []
cnt = 0
temp = 0

# 처음 시간초과났던 함수
def schedule(arr):
  global cnt
  for i in range(n):
    for j in range(i+1,n): 
      if arr[i][1] <= arr[j][0]:
        cnt += 1
        arr[i][1] = arr[j][1]
    res.append(cnt)
    cnt = 1
  print(max(res))

n = int(stdin.readline())
for i in range(n):
  start,end = map(int, stdin.readline().split())
  meeting.append([start,end])
meeting.sort()
meeting.sort(key = lambda x:x[1])

for start, end in meeting:
  if start >= temp:
    cnt += 1
    temp = end

print(cnt)
```
### 결과
성공
### 접근
처음에 회의 시작시간을 기준으로 정렬한 후, 현재회의 끝시각과 다음 회의 시작시각을 비교하고자 하였다. 그러나 회의 시간 비교과정에 이중 for문사용으로 인한 시간초과가 나와 다시 생각하게 되었다. 

두번째로 생각한 방법은 회의 시작시각으로 정렬후 회의가 끝나는 시각으로 다시한번 정렬하는 방법이였다. 먼저 시작시각으로 정렬한 이유는 만약 회의 시간이 (1,2) (2,2) 가 있을 때, 시작시각이 더 빠른 순으로 정렬하면 2개의 회의진행이 가능하기 때문이다. 그리고 회의 종료시각으로 한번 더 정렬한 이유는 시작시각이 같을 때, 회의가 더 빨리 끝난다면 더 많은 회의를 할 수 있는 기회가 생길 것이라 생각했기 때문이다. 

## 문제 회고
문제 난이도가 올라갈수록 시간복잡도가 중요해지는 것을 요즘 느끼는 중입니다. 

# 13334 : 철로
### code
```python
import sys
import heapq

n = int(sys.stdin.readline())
road_info = []
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)

d = int(sys.stdin.readline())
roads = []
for road in road_info:
    house, office = road
    if abs(house - office) <= d:
        road = sorted(road)
        roads.append(road)
roads.sort(key=lambda x:x[1])

answer = 0
heap = []
for road in roads:
    if not heap:
        heapq.heappush(heap, road)
    else:
        while heap[0][0] < road[1] - d:
            heapq.heappop(heap)
            if not heap:
                break
        heapq.heappush(heap, road)
    answer = max(answer, len(heap))

print(answer)
```
### 결과
실패 (아이디어구상 실패)
### 접근
접근방법조차 생각하지못했다. 1주차 3번째 문제인 "전구와 스위치" 이후로 손도 대지못한 문제였다ㅠㅠ 결국 구글을 보고 배울 수 밖에 없었다.

## 문제 회고
이렇게 막히는 문제를 만났을 때, 막연하게 관련 개념들을 더 공부하겠다고 하고, 찡찡대는 내 자신이 싫어진다ㅋㅋㅋ 그럴 때마다 나에게 "어쩌라고"를 외친 후 해야할 일을 할 뿐이다..
# 1202 : 보석도둑
### code
```python
import heapq
import sys

dia = []
bag = []
res = 0

n,k = map(int,sys.stdin.readline().split())

for i in range (n):
  heapq.heappush(dia, list(map(int, sys.stdin.readline().split())))

for i in range(k):
  bag.append(int(sys.stdin.readline()))

bag.sort()
temp = []

for i in (bag):
  while dia and i >= dia[0][0]:
    heapq.heappush(temp,-heapq.heappop(dia)[1])
  if temp:
    res -= heapq.heappop(temp)
  elif not dia:
    break

print(res)
```
### 결과
실패 (시간초과)
### 접근
보석의 가격을 높은 순으로 정렬 후, 가방의 용량보다 무게가 가벼우면서 가격이 가장 비싼 보석의 값을 담은 후, 그 보석은 제거하는 것으로 접근했다.
이때, "용량이 작은 가방부터 담아야 한다." 이 문장을 구현하기 위해서 가방의 용량과 보석의 무게, 가격을 비교하는 이중 for문을 작성해보기도하고, 별의 별짓을 다 해봤지만 결과는 시간초과가 나왔다.
그래서 결국 구글 검색을 통해 최소힙과 최대힙구조를 사용해야한다는 것을 배웠다.
## 문제회고
자료구조를 배우지 않은 것이 아닌데, 문제를 풀 때 활용할 생각을 하지 못한다.
내가 알고 있는 개념을 적재적소에 활용하는 능력을 키울 필요를 느꼈다.