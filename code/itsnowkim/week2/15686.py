from itertools import combinations

n,m = map(int,input().split())
data = []
chicken = []
city = []
for _ in range(n):
    data.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            city.append((i,j))
        if data[i][j] == 2:
            chicken.append((i,j))
ans = float("inf")
chicken_s = list(combinations(chicken,m))
for candidate in chicken_s:
    city_dist =0
    for j in range(len(city)):
        dist =float("inf")
        for x,y in candidate:
            dist = min(dist,abs(x-city[j][0])+abs(y-city[j][1]))
        city_dist+=dist
    ans = min(ans,city_dist)

print(ans)