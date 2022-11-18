import sys

read = sys.stdin.readline

m, n = map(int, read().split())
lst = list(map(int, read().split()))

start = 1
end = max(lst)  # 과자 최대 길이
res = 0


# l 길이로 쪼갤때 나오는 과자의 총 개수
def cookie_count(l):
    cnt = 0
    for cookie in lst:
        cnt += cookie // l
    return cnt


# 나눠주는 길이 이분탐색
while start <= end:
    mid = (start + end) // 2
    if cookie_count(mid) >= m:  # 길이 더 키울 수 있음
        res = mid  # 되는 경우에 답 미리 저장
        start = mid + 1
    else:  # 나눠주는 길이 줄여야함
        end = mid - 1

print(res)
