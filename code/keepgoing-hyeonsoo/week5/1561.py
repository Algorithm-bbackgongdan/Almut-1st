import sys

read = sys.stdin.readline

n, m = map(int, read().split())
times = list(map(int, read().split()))

start = 0
end = 2000000000 * 30


def count_children(full_time):
    cnt = m
    for time in times:
        cnt += full_time // time
    return cnt


if n <= m:
    print(n)
else:
    while start <= end:
        mid = (start + end) // 2
        if count_children(mid) >= n:  # 모든 아이들이 최소 한 번 이상씩 놀이기구 탐
            optimal_time = mid  # 이분탐색 끝나면 모든 아이들이 정확히 한 번씩 타게되는 최적의 시간이 구해짐
            end = mid - 1
        else:  # 놀이기구 안 탄 아이 존재 => full_time 늘려야함
            start = mid + 1

    # (optimal_time - 1) 까지 탑승한 아이들의 숫자 계산
    cur_children = count_children(optimal_time - 1)

    # optimal_time 에 탑승한 아이 계산
    for i in range(m):
        if optimal_time % times[i] == 0:  # optimal_time 에 탑승한 아이
            cur_children += 1
        if cur_children == n:
            print(i + 1)
            break
