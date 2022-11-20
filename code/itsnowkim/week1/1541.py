a = input()

asplit = a.split('-')

# split된 각각 계산
templist=[]
for formula in asplit:
    b = formula.split('+')
    temp=0
    for number in b:
        temp += int(number)
    templist.append(temp)

# minus 계산
res = templist[0]
for idx in range(1, len(templist)):
    res -= templist[idx]

print(res)