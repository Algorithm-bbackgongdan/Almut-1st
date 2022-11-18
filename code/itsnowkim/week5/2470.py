# 5
# -2 4 -99 -1 98

import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

# 정렬
arr.sort()

start = 0
end = len(arr) -1
answer = (0,0)
ans = 9999999999

while start < end:
    left = arr[start]
    right = arr[end]

    # 섞어
    total = left + right

    if abs(total) < ans:
        ans = total
        answer = (left, right)
    
    # 끝!
    if total == 0:
        break
    elif total < 0:
        start += 1
    else:
        end -= 1

print(answer[0], answer[1])
        




    
