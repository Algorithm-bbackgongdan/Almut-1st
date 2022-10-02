import sys

read = sys.stdin.readline

n = int(read())
lst = list(map(int, read().rstrip()))
goal = list(map(int, read().rstrip()))


def turn(A, B):
    L = A[:]
    press = 0
    for i in range(1, n):
        if L[i - 1] == B[i - 1]:
            continue
        press += 1
        for j in range(i - 1, i + 2):
            if j < n:
                L[j] = 1 - L[j]
    if L == B:
        return press
    else:
        return 1e9


# 첫 번째 전구 스위치 안 누르는 경우
res1 = turn(lst, goal)

# 첫 번째 전구 스위치 누르는 경우
lst[0] = 1 - lst[0]
lst[1] = 1 - lst[1]
res2 = turn(lst, goal)

res = min(res1, res2 + 1)

if res != 1e9:
    print(res)
else:
    print(-1)
