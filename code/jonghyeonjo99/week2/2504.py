a = input()
stack = []
res = 0
temp = 1
count1 = count2 = count3 = count4 = 0

for i in range(len(a)):
  if a[i] == "(":
    count1 += 1
  elif a[i] == ")":
    count2 += 1
  elif a[i] == "[":
    count3 += 1
  else:
    count4 +=1
if count1 != count2 or count3 != count4:
  print(0) #(,[의 숫자와 ],)의 숫자가 다르면 짝이 맞지않는다.

else:
  for i in range(len(a)):
    if a[i] == "(":
      stack.append(a[i])
      temp *= 2
    elif a[i] == "[":
      stack.append(a[i])
      temp *= 3
    elif a[i] == ")":
      if a[i-1] == "(":
        res += temp
      stack.pop()
      temp //= 2
    else:
      if a[i-1] == "[":
        res += temp
      stack.pop()
      temp //= 3
  print(res)