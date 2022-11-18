import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 1 ~ 30 사이 자연수 -> 미리 배열 만들어 놓고 세기!

if n < m:
    print(n)
    sys.exit(0)

# naive 한 방법
order = 1
time = min(arr)

# 한 iteration에서 한 명씩 나가도록
