# 1561 : 놀이 공원
import sys

def solve(N, M, L):
    if N <= M:
        print(N)
        return
    MAX_N = 2000000000  # N : 1 ~ 20억
    start, end = 0, 30 * MAX_N  # 탐색 가능한 최대 시간

    # N번째 아이가 탑승 가능한 최소 시간(분) 탐색
    T = 0
    riding = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for l in L:
            cnt += mid // l
            cnt += 1 if mid % l else 0
        if cnt > N:
            end = mid - 1
        else:
            start = mid + 1
            T = mid
            riding = cnt

    # 만약 N번째 아이까지 전부 탑승한 시간 T를 구했다면, N이 탑승 가능한 최소 시간 탐색
    while riding == N:
        T -= 1
        cnt = 0
        for l in L:
            cnt += T // l
            cnt += 1 if T % l else 0
        riding = cnt
  
    # T분에 몇 번째 놀이기구를 타는지 탐색
    order = N - riding - 1  # 남아있는 사람 중 N이 탈 순서 (0부터 시작)
    rides = []  # 0 ~ order 번까지 몇 번 기구를 타는지 저장
    for i in range(len(L)):
        if T % L[i] == 0:
            rides.append(i + 1)  # 기구의 번호 (i+1) 저장
    print(rides[order])
    return


N, M = map(int, sys.stdin.readline().rstrip().split())
L = list(map(int, sys.stdin.readline().rstrip().split()))
solve(N, M, L)