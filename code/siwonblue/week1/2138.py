import copy

n = int(input())
data1 = list(map(int,list(input())))
target = list(map(int,list(input())))
ans = []

def solve(data1):
    case1 = copy.deepcopy(data1)
    case2 = copy.deepcopy(data1)
    cnt1 = 1
    cnt2 = 0
    # 처음 건들기
    case1[0] = (case1[0] + 1) % 2
    case1[1] = (case1[1] + 1) % 2
    test1=0
    test2=0
    for i in range(1, len(case1)):
        test1+=1
        if (case1[i - 1] != target[i - 1]) and i != len(case1) - 1:  # 가운데 경우
            case1[i - 1] = (case1[i - 1] + 1) % 2
            case1[i] = (case1[i] + 1) % 2
            case1[i + 1] = (case1[i + 1] + 1) % 2
            cnt1 += 1
        elif (case1[i - 1] != target[i - 1]) and i == len(case1) - 1:  # 마지막인 경우
            case1[i - 1] = (case1[i - 1] + 1) % 2
            case1[i] = (case1[i] + 1) % 2
            cnt1 += 1
    if case1 == target:
        # print('case1', case1)
        ans.append(cnt1)

    for i in range(1, len(case2)):
        test2 += 1
        if (case2[i - 1] != target[i - 1]) and i != len(case2) - 1:  # 가운데 경우
            case2[i - 1] = (case2[i - 1] + 1) % 2
            case2[i] = (case2[i] + 1) % 2
            case2[i + 1] = (case2[i + 1] + 1) % 2
            cnt2 += 1
        elif (case2[i - 1] != target[i - 1]) and i == len(case2) - 1:  # 마지막인 경우
            case2[i - 1] = (case2[i - 1] + 1) % 2
            case2[i] = (case2[i] + 1) % 2
            cnt2 += 1
    if case2 == target :
        # print('case2',case2)
        ans.append(cnt2)
    # print('test1 :',test1)
    # print('test2 :',test2)
    # print('ans   :',ans)


solve(data1)
if len(ans)==0:
    print(-1)
else:
    print(min(ans))
