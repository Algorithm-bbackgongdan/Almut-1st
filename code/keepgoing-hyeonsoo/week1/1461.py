import sys

read = sys.stdin.readline

n, m = map(int, read().split())
books = list(map(int, read().split()))
minn = 10001
now = 0
res = 0


while len(books) > 0:
    for i in range(len(books)):
        if abs(books[i] - now) < minn:
            minn = abs(books[i] - now)
            minn_idx = i
    res += minn
    now = books[i]
    del books[minn_idx]


print(res)
