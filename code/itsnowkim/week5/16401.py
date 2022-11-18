# 3 10
# 1 2 3 4 5 6 7 8 9 10

# ans: 8

# 4 3
# 10 10 15
# ans : 7

import sys

m, n = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(arr)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    # 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없을 때
    if mid == 0:
        total = 0
        break
    
    # 모든 과자에 대해 탐색
    # 중간값보다 크거나 같으면 자른다.
    for x in arr:
        if x >= mid:
            total += (x//mid)

    # 나눠줄 수 있는 개수가 더 많다 -> 더 크게 자른다
    if total >= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)