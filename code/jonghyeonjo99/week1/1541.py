a = input().split('-') # -를 기준으로 나누기
res = []
for i in a:
  sum = 0
  b = i.split('+') # 더할 숫자들
  for j in b:
    sum += int(j)
  res.append(sum)
  
num = res[0]
for i in range(1,len(res)):
  num -= res[i]
print(num)