import sys

read = sys.stdin.readline

n, m = map(int, read().split())
books = list(map(int, read().split()))

plus = []
minus = []
maxx = -1e9
res = 0

for book in books:
    if book > 0:
        plus.append(book)
    else:
        minus.append(abs(book))
    if abs(book) > maxx:
        maxx = abs(book)

plus.sort(reverse=True)
minus.sort(reverse=True)

for i in range(0, len(plus), m):
    if plus[i] == maxx:
        res += plus[i]
    else:
        res += plus[i] * 2

for i in range(0, len(minus), m):
    if minus[i] == maxx:
        res += minus[i]
    else:
        res += minus[i] * 2

print(res)
