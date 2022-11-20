import sys

read = sys.stdin.readline

a = read().split("-")
num = []
for item in a:
    temp = 0
    b = item.split("+")
    for c in b:
        temp += int(c)
    num.append(temp)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)
