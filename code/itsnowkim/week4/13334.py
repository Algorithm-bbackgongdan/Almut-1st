# 최대 철로 길이
MAXIMUM = 200000000
n = int(input())
sett = []
for _ in range(n):
    h, o = map(int, input().split())
    # 둘 중 작은 값을 먼저 넣기
    if o < h:
        sett.append((o, h))
    else:
        sett.append((h, o))

# 철로의 길이 input
d = int(input())

# 시작점 기준으로 정렬
a = sorted(sett, key=lambda x:(x[0], x[1]))

max_count = 0
temp_count = 0
start_point = MAXIMUM
end_point = MAXIMUM

for idx, item in enumerate(a):
    # print(item)
    if item[1] - item[0] <= d:
        if idx == 0:
            temp_count += 1
            start_point = item[0]
            end_point = item[1]
        elif item[1] - start_point <= d and item[0] <= end_point:
            temp_count += 1
            max_count = max(max_count, temp_count)
        else:
            temp_count = 1
            start_point = item[0]
            end_point = item[1]
    # 애초에 철로에 겹치지 않음
    else:
        temp_count = 0
        start_point = item[0]
        end_point = item[1]

print(max_count)