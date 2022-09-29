import sys

N_ = int(sys.stdin.readline().rstrip())
orig_ = list(map(int, sys.stdin.readline().rstrip()))
target_ = list(map(int, sys.stdin.readline().rstrip()))


def flip(a):
    return 0 if a else 1


def calc(clickFirst, orig, target, N):
    count = 0
    if clickFirst:
        orig[0] = flip(orig[0])
        orig[1] = flip(orig[1])
        count += 1
    for i in range(1, N - 1):
        if orig[i - 1] == target[i - 1]:
            pass
        else:
            orig[i - 1] = flip(orig[i - 1])
            orig[i] = flip(orig[i])
            orig[i + 1] = flip(orig[i + 1])
            count += 1

    if orig[-1] != target[-1]:
        orig[-1] = flip(orig[-1])
        orig[-2] = flip(orig[-2])
        count += 1

    return count, orig == target


res1_c, res1 = calc(True, orig_.copy(), target_.copy(), N_)
res2_c, res2 = calc(False, orig_.copy(), target_.copy(), N_)

if res1 and res2:
    print(min(res1_c, res2_c))
elif res1:
    print(res1_c)
elif res2:
    print(res2_c)
else:
    print(-1)