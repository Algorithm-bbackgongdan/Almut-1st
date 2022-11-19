import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 1 ~ 30 사이 자연수 -> 미리 배열 만들어 놓고 세기!

if n < m:
    print(n)
    sys.exit(0)

# 이분 탐색
left, right = 0, 60000000000
t = None
while left <= right:
    mid = (left + right) // 2
    cnt = m
    for i in range(m):
        cnt += mid // arr[i]
    if cnt >= n:  # n명을 태울 수 있는 상황
        t = mid
        right = mid - 1
    else:
        left = mid + 1

# t - 1에 탑승한 아이들의 숫자를 계산한다.
cnt = m
for i in range(m):
    cnt += (t - 1) // arr[i]

# t에 탑승한 아이를 계산한다.
for i in range(m):
    if t % arr[i] == 0:  # t 시간에 탑승한 아이
        cnt += 1
    if cnt == n:
        print(i + 1)
        break