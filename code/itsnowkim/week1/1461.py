from collections import deque

n,m = map(int,input().split())
a = list(map(int, input().split()))
a.sort()
book = deque(a)

# 음수, 양수 나누기
neg = deque()
pos = deque()
for item in book:
    if item < 0:
        neg.append(item)
    elif item > 0:
        pos.append(item)

res = 0
# 가장 먼 곳부터 제거
if abs(book[0]) > abs(book[-1]):
    res += abs(neg[0])
    # m개만큼 pop
    for i in range(m):
        if len(neg) == 0:
            break
        neg.popleft()
else:
    res += pos[-1]
    # m개만큼 pop
    for i in range(m):
        if len(pos) == 0:
            break
        pos.pop()

# 남은 것들은 *2 해야 함
while pos:
    res += pos[-1] * 2
    # m개만큼 pop
    for i in range(m):
        if len(pos) == 0:
            break
        pos.pop()

# 남은 것들은 *2 해야 함
while neg:
    res += abs(neg[0]) * 2
    # m개만큼 pop
    for i in range(m):
        if len(neg) == 0:
            break
        neg.popleft()

print(res)
