# 치킨 배달
# 22.10.4
# 구현

from itertools import combinations

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]


# 치킨 집과 집 넣어 주면 도시의 치킨 거리 출력해주는 함수
def city_distance(home,bbq):
    city = []
    for a in home:
        test = []  # 집에서 모든 치킨 집에 대한 거리
        for b in bbq:
            test.append(abs(a[0] - b[0]) + abs(a[1] - b[1]))
        # print('test',test)
        city.append(min(test))  # 치킨 거리
    return sum(city)  # 도시의 치킨 거리

def solve(data):
    # 치킨집과 집의 위치 인덱스 뽑아내기
    bbq = []
    home = []
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            if v == 1:
                home.append([i+1,j+1])
            elif v == 2:
                bbq.append([i+1,j+1])
    # print('치킨집 위치',bbq)
    # print('집 위치',home)

    # 치킨집이 x 개가 있고 m 개만 남겨야 하면
    # 나올 수 있는 치킨 집의 개수는 xCm 개가 된다.
    # 그 각각의 경우의 수에 대해 모두 거리를 구하고 최소값을 모으고 그 중 다시 최소값 찾기

    # 남길 치킨 집 경우의 수
    lists = list(combinations(bbq,m))
    res = []
    for one in lists:
        # print('combination : ',a)
        res.append(city_distance(home, one))
    print(min(res)) # len([17, 18, 15, 10, 22, 21, 15, 22, 17, 17]) == xCm
solve(data)




