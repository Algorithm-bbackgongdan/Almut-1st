# 미완성
# 고민했는데 잘 안 풀려서 좀만 더 트라이해볼게요..

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
