N, K = map(int, input().split())
jewl = []
bag = []
for _ in range(N):
    m, v = map(int, input().split())
    jewl.append((m,v))
for _ in range(K):
    bag.append(int(input()))
# sort by value, not weight
jewl = sorted(jewl, key=lambda x: x[1])
for j in jewl:
    print(j)

for b in bag:
    print(b)