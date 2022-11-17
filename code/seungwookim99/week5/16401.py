# 16401 : 과자 나눠주기
import sys

M, N = map(int, sys.stdin.readline().rstrip().split())
L = list(map(int, sys.stdin.readline().rstrip().split()))

start, end = 1, max(L)
res = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for l in L:
        count += (l // mid)
    if count >= M:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)