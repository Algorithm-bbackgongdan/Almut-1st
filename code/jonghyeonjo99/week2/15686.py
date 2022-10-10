import itertools

n,m = map(int,input().split())
arr = []
num1 = [] # 집 
num2 = [] # 치킨

for i in range(n):
  arr.append(list(map(int,input().split())))

for i in range(n):
  for j in range(n):
    if arr[i][j] == 1:
      num1.append(i+1)
      num1.append(j+1)
    elif arr[i][j] == 2:
      num2.append(i+1)
      num2.append(j+1)

num1_index = [num1[i*2:(i+1)*2] for i in range((len(num1)+1)//2)] #집 좌표
num2_index = [num2[i*2:(i+1)*2] for i in range((len(num2)+1)//2)] #치킨 좌표

com = list(itertools.combinations((num2_index),m)) #치킨집 m개 조합

num = 0
for i in range(len(num1_index)):
  minimal = []
  for j in range(0,m):
    list =[]
    temp = abs(num1_index[i][0] - com[i][j][0]) + abs(num1_index[i][1] - com[i][j][1])
    list.append(temp)
  res = min(list) #집x와 치킨집 사이의 치킨거리.
  num += res #도시의 치킨거리
  minimal.append(num)
print(min(minimal))
      


