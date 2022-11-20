import sys

read = sys.stdin.readline

n = int(input())
lst = [list(map(int, read().split())) for _ in range(n)]
lst.sort(key=lambda x: (x[1], x[0]))  # 두 번째 원소 기준으로 정렬

end = 0
cnt = 0
for s, e in lst:
    if end <= s:
        cnt += 1
        end = e

print(cnt)
