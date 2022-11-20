import sys

START, END = 0, 1

N = int(sys.stdin.readline().rstrip())
Times = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    Times.append((s, e))

Times = sorted(Times, key=lambda x: (x[1], x[0]))  # 종료시간으로 정렬
count = 1
end = Times[0][END]
for i in range(1, N):
    if Times[i][START] >= end:
        count += 1
        end = Times[i][END]
    else:
        continue

print(count)