# 알파벳
# 22.11.4

import sys
read=sys.stdin.readline
r,c=map(int,read().split())

alpabet = [ list(input()) for _ in range(r)]
temp = []
for v in alpabet:
  temp+=v
temp = list(set(temp))
print(temp)

