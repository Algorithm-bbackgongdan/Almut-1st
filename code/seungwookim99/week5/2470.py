# 2470 : 두 용액
import sys

N = int(sys.stdin.readline().rstrip())
L = list(map(int, sys.stdin.readline().rstrip().split()))
M, P = [], []
for l in L:
    if l > 0:
        P.append(l)
    else:
        M.append(l)
P.sort()
M.sort(reverse=True)

if len(M) == 0:
    res = [P[0], P[1]]
elif len(P) == 0:
    res = [M[0], M[1]]
else:
    S = float('inf')
    i, j = 0, 0
    res = [M[i], P[j]]
    while i < len(M) and j < len(P):
        if abs(M[i] + P[j]) < abs(S):
            S = M[i] + P[j]
            res = [M[i], P[j]]
        if M[i] + P[j] >= 0:
            i += 1
        else:
            j += 1
    if len(P) >= 2 and abs(P[0] + P[1]) < abs(S):
        res = [P[0], P[1]]
    elif len(M) >= 2 and abs(M[0] + M[1]) < abs(S):
        res = [M[1], M[0]]

print(min(res), max(res))