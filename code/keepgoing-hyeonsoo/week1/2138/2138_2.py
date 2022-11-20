import sys

read = sys.stdin.readline

n = int(read())
bulb = list(map(int, read().rstrip()))
goal = list(map(int, read().rstrip()))


def turn(bulb, goal):
    res = 0
    # 두 번째 ~ 끝에서 두 번째 전구까지
    for i in range(1, n - 1):
        if bulb[i - 1] != goal[i - 1]:
            bulb[i - 1], bulb[i], bulb[i + 1] = (
                int(not bulb[i - 1]),
                int(not bulb[i]),
                int(not bulb[i + 1]),
            )
            res += 1

    # 맨 끝 전구 예외 처리
    if bulb[n - 2] != goal[n - 2]:
        bulb[n - 2], bulb[n - 1] = int(not bulb[n - 2]), int(not bulb[n - 1])
        res += 1

    if bulb == goal:  # 원하는 결과와 같을 때
        return res
    else:  # 원하는 결과와 다를 때
        return 1e9


# 첫 번째 전구 스위치 킨 경우
bulb_1 = bulb.copy()
bulb_1[0], bulb_1[1] = int(not bulb_1[0]), int(not bulb_1[1])

res_1 = turn(bulb_1, goal)

# 첫 번째 안 킨 경우
bulb_2 = bulb.copy()
res_2 = turn(bulb_2, goal)

# 결과 계산
ans = min(res_1 + 1, res_2)

if ans == 1e9:  # 불가능한 경우
    print(-1)
else:  # 가능한 경우
    print(ans)
