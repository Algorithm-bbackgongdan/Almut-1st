# 가장 빨리 끝나는 회의부터 순차적으로 담으면 그게 제일 성능이 좋음

N = int(input())
sett = []
for _ in range(N):
    s, e = map(int, input().split())
    sett.append((s,e))

# 끝나는 시간 기준으로 정렬
a = sorted(sett, key=lambda x:(x[1], x[0]))

result = []
for item in a:
    # 가장 빨리 끝나는 회의 넣기
    if not result:
        result.append(item)
    else:
        # 순차적으로 넣기
        if item[0] >= result[-1][1]:
            result.append(item)

print(len(result))