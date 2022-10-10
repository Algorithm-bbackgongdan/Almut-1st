# 미완성
# 고민했는데 잘 안 풀려서 좀만 더 트라이해볼게요..

import sys

read = sys.stdin.readline

lst = list(read().rstrip())  # 원본 문자열

stack = []  # 여는 괄호 저장할 스택
ans = 0  # 최종 정답
temp = 1

for i in range(len(lst)):

    # '(' 들어오면 스택에 추가하고 temp 에 2 곱함
    if lst[i] == "(":
        stack.append("(")
        temp *= 2

    # '[' 들어오면 스택에 추가하고 temp 에 3 곱함
    elif lst[i] == "[":
        stack.append("[")
        temp *= 3

    # ')' 들어올 때
    elif lst[i] == ")":
        if not stack or stack[-1] != "(":  # stack 이 없거나, stack top 이 '(' 가 아니라면 탈출
            ans = 0
            break
        elif lst[i - 1] == "(":  # 직전 문자가 '(' 일 때만 ans 에 temp 더함
            ans += temp

        # 공통 (ex. stack[-1] == '(' 이여도 lst[-1] == ']' 나 ')' 인 경우 )
        stack.pop()
        temp //= 2  # 괄호 쌍이 하나 끝났으므로 2 다시 나눠줌

    # ']' 들어올 때
    elif lst[i] == "]":
        if not stack or stack[-1] != "[":  # stack 이 없거나, stack top 이 '[' 가 아니라면 탈출
            ans = 0
            break
        elif lst[i - 1] == "[":  # 직전 문자가 '[' 일 때만 ans 에 temp 더함
            ans += temp

        # 공통
        stack.pop()
        temp //= 3  # 괄호 쌍이 하나 끝났으므로 3 다시 나눠줌

if stack:  # for문 끝났는데 stack 남아있으면 0 출력
    print(0)
else:
    print(ans)
