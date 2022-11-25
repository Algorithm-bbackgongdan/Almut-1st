input_list = list(input())

check = []
answer = 0
temp = 1
prev = ''

for item in input_list:
    if item == '(' or item == '[':
        check.append(item)
        prev = item
        if item == '(':
            temp *= 2
        if item == '[':
            temp *= 3

    elif item == ']':
        if len(check) == 0 or check[-1] != '[':
            answer = 0
            break
        
        # add to answer
        if prev == '[':
            answer += temp
            prev=''
        temp /= 3
        check.pop()
    elif item == ')':
        if len(check) == 0 or check[-1] != '(':
            answer = 0
            break
        
        # add to answer
        if prev == '(':
            answer += temp
            prev=''
        temp /= 2
        check.pop()

if len(check) != 0:
    answer = 0
print(int(answer))