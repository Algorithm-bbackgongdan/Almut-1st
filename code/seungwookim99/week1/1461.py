import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
books = list(map(int, sys.stdin.readline().rstrip().split()))
cost = 0
books.sort()
m = [0]  # 음수 list
p = [0]  # 양수 list


def add_cost_and_pop(cost, arr, M, isFirst):
    cost += arr[-1] if isFirst else 2 * arr[-1]
    if len(arr) >= M:
        for _ in range(M):
            arr.pop()
    else:
        arr = []
    return cost, arr


for b in books:
    if b < 0:
        m.append(-b)
    else:
        p.append(b)
m.sort()

isFirst = True
while m and p:
    if m[-1] > p[-1]:
        cost, m = add_cost_and_pop(cost, m, M, isFirst)
    else:
        cost, p = add_cost_and_pop(cost, p, M, isFirst)
    isFirst = False

while m:
    cost, m = add_cost_and_pop(cost, m, M, isFirst)

while p:
    cost, p = add_cost_and_pop(cost, p, M, isFirst)
print(cost)