

data = list(input().split('-'))

def solve(data):
    minus = 0
    ans = 0
    if '+' in data[0]:

        data[0] = sum(list(map(int, data[0].split('+'))))
        ans = data[0]
    else:
        data[0] = int(data[0])
        ans = data[0]
    for i in range(1,len(data)):
        data[i] = list(map(int,data[i].split('+')))
        data[i] = sum(data[i])
        minus += data[i]
    ans -=  minus
    return ans
print(solve(data))
