import sys

N = int(input())
# input data
arr = list(map(int, sys.stdin.readline().split()))

# 증가하는 순열의 개수를 담은 리스트
# 모든 숫자는 자기 자신이 순열이 될 수 있으므로
# 최소는 1, 모두 1로 초기화
ans = [1] * len(arr)

# 앞에서부터 dp 채우기
for i in range(N):
    # 자기보다 앞에 있는 원소에 대해서만 체크 필요
    for j in range(i):
        # 나보다 작은경우만 고려
        # dp 배열에서 ans[i] == ans[j] 인 경우는 arr[i]가 arr[j]의 증가하는 순열에서 직전의 수라는 뜻이고
        # ans[i] < ans[j] 인 경우는 명백하게 순열의 일부이므로 ans[j]에 1을 더해주면 된다. 
        if arr[i] > arr[j] and ans[i] <= ans[j]:
            ans[i] = ans[j] + 1
    
print(max(ans))