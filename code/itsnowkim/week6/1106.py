import sys

C, N = map(int, sys.stdin.readline().split())
hotel = []
for _ in range(N):
    c, p = map(int, sys.stdin.readline().split())
    hotel.append([c, p])

# 조건에 맞게 먼저 정렬
hotel = sorted(hotel, key=lambda x: x[0]/x[1])

# 2차원 배열 생성 : (N*비용의 최댓값)
row = hotel[-1][0] * C
# 비용을 담는 배열. 무조건 이 index 내에 정답 존재
dp = [[0 for _ in range(row)] for _ in range(N)]
# print(hotel)

# 초기화
for i in range(N):
    dp[i][1] = (i // hotel[i][0]) * hotel[i][1]
for i in range(row):
    dp[0][i] = (i // hotel[0][0]) * hotel[0][1]

# dp 테이블 채우기
for i in range(1, N):
    for j in range(1,row):
        if dp[i][j-1] < dp[i-1][j]:
            # print('위가 더 큼')
            dp[i][j] = dp[i-1][j]

        elif dp[i][j-1] > dp[i-1][j]:
            # print('왼쪽이 더 큼')
            k = j
            while dp[i][k-1] == dp[i][j-1] and k >= 0:
                k -= 1
            # 차이만큼 더해주기
            dp[i][j] = dp[i][j-1] + hotel[i][1] * ((j - k) // hotel[i][0])
        else:
            # print('같음')
            # 같음. 딱 맞는 곳까지(최소로 넣는 곳이 어딘지) 찾아가야됨
            # 위의 끝으로 먼저 이동
            k = i
            while dp[k-1][j] == dp[i-1][j] and k >= 0:
                k -= 1
            # 왼쪽 끝으로 이동
            q = j
            while dp[k][q-1] == dp[k][j-1] and q >= 0:
                q -= 1
            
            # dp[k][q] 얘가 최소임.
            # 얘의 cost와 지금의 cost 차이만큼 더 집어넣을 수 있음.
            dp[i][j] = dp[i][j-1] + hotel[i][1] * ((j - q)//hotel[i][0])
        # 새로운 cost 넘어가기 전 이전 cost가 만족하는지 확인하기
        if dp[i][j] >= C:
            print(j)
            sys.exit(0)
        







# print(c, n)
# print(hotel)