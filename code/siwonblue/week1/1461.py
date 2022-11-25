
# 데이터 입력
n, m = map(int, input().split())
data = list(map(int, input().split()))
first = [] # 가장 큰 값이 존재하는 리스트
second = [] # 큰 값이 없는 리스트
# 데이터 전처리
for val in data:
    if val > 0:
        first.append(val)
    else:
        second.append(abs(val))
first.sort(reverse=True)
second.sort(reverse=True)

# print('first',first)
# print('second',second)

# 알고리즘 적용
def solve(first,second):
    test = []
    for val in range(0,len(first),m):
        test.append(first[val])
    for val in range(0,len(second),m):
        test.append(second[val])
    ans = max(test)
    test.remove(max(test))
    ans += sum(test)*2
    print(ans)
solve(first,second)
