# 미완성

import sys

read = sys.stdin.readline

string = list(read().rstrip())

stack = []
res = 0
temp = 1

for i in range(len(stack)):
    if string[i] == "(":
        stack.append(string[i])

    elif string[i] == "[":
        stack.append(string[i])

    elif string[i] == ")":
        if not stack or stack[-1] == "[":
            break
