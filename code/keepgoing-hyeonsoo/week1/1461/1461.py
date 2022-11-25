import sys

read = sys.stdin.readline

n, m = map(int, read().split())
books = list(map(int, read().split()))
res = 0
plus = []
minus = []
maxx = 0

for book in books:
    if book > 0:
        plus.append(book)
    else:
        minus.append(book)

    if abs(book) > abs(maxx):
        maxx = book

plus.sort(reverse=True)
minus.sort()

distances = []

for i in range(0, len(plus), m):
    if plus[i] != maxx:
        distances.append(plus[i])

for i in range(0, len(minus), m):
    if minus[i] != maxx:
        distances.append(minus[i])

res = abs(maxx)
for i in distances:
    res += abs(i * 2)

print(res)
