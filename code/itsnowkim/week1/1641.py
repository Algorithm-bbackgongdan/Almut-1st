from collections import deque

n,m = map(int,input().split())
a = list(map(int, input().split()))
a.sort()
book = deque(a)

res = 0
# 가장 먼 곳부터 제거
if abs(book[0]) > abs(book[-1]):
    res += abs(book[0])
    # m개만큼 pop
    for i in range(m):
        if len(book) == 0:
            break
        if book[0] > 0:
            break
        book.popleft()
else:
    res += abs(book[-1])
    # m개만큼 pop
    for i in range(m):
        if len(book) == 0:
            break
        if book[-1] < 0:
            break
        book.pop()

# 남은 것들은 *2 해야 함
while book:
    if abs(book[0]) >= abs(book[-1]):
        res += abs(book[0]) * 2
        # m개만큼 pop
        for i in range(m):
            if len(book) == 0:
                break
            if book[0] > 0:
                break
            book.popleft()
    else:
        res += abs(book[-1]) * 2
        # m개만큼 pop
        for i in range(m):
            if len(book) == 0:
                break
            if book[-1] < 0:
                break
            book.pop()

print(res)
