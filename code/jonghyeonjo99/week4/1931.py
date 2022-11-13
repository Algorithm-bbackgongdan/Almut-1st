from sys import stdin

meeting = []
res = []
cnt = 0
temp = 0

# 처음 시간초과났던 함수
def schedule(arr):
  global cnt
  for i in range(n):
    for j in range(i+1,n): 
      if arr[i][1] <= arr[j][0]:
        cnt += 1
        arr[i][1] = arr[j][1]
    res.append(cnt)
    cnt = 1
  print(max(res))

n = int(stdin.readline())
for i in range(n):
  start,end = map(int, stdin.readline().split())
  meeting.append([start,end])
meeting.sort()
meeting.sort(key = lambda x:x[1])

for start, end in meeting:
  if start >= temp:
    cnt += 1
    temp = end

print(cnt)
