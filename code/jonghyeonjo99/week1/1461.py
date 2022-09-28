import sys
input = sys.stdin.readline

n,m = list(map(int,input().split()))
place = list(map(int,input().split()))

num1 = [0] #음수
num2 = [0] #양수

for i in range(n):
  if place[i] < 0:
    num1.append(place[i])
  else:
    num2.append(place[i])

num1.sort()
num2.sort(reverse=True)

com = -num1[0] #절대값 비교를 위해

if com > num2[0]: #음수 절대값이 더 클 때
  res = 0
  for i in range(m,len(num1),m):
    num = -num1[i]
    res += num * 2
  for j in range(0,len(num2),m):
    res += num2[j] * 2
  res += com
  print(res)

else:
  res = 0
  for i in range(0,len(num1),m):
    num = -num1[i]
    res += num * 2
  for j in range(m,len(num2),m):
    res += num2[j] * 2
  res += num2[0]
  print(res)

#시간초과