import sys

s = list(sys.stdin.readline().rstrip())


def solve(s):
    sum = [0 for _ in range(31)]
    stack = []
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return 0
            stack.pop()
            l = len(stack)
            if sum[l + 1] == 0:
                sum[l] += 2
            else:
                sum[l] += sum[l + 1] * 2
                sum[l + 1] = 0
        elif i == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return 0
            stack.pop()
            l = len(stack)
            if sum[l + 1] == 0:
                sum[l] += 3
            else:
                sum[l] += sum[l + 1] * 3
                sum[l + 1] = 0
    return 0 if len(stack) else sum[0]


print(solve(s))
