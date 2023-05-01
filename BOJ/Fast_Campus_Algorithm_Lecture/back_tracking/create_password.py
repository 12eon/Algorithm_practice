from itertools import combinations

n,c = map(int, input().split())

alpha = list(input().split())
beta = []

m = ['a','e','i','o','u']
i = 0
while i < len(alpha):
    if alpha[i] in m:
        beta.append(alpha[i])
        alpha.pop(i)
    else:
        i += 1

check = []
for i in range(2, n):
    if i <= len(alpha) and n-i <= len(beta):
        check.append([i, n-i])

def calc(n):
    global result
    a = list(combinations(alpha, n[0]))
    b = list(combinations(beta, n[1]))
    for i in a:
        for j in b:
            cmp = list(i) + list(j)
            cmp.sort()
            result.append(cmp)

result = []
for c in check:
    calc(c)

result.sort()
for r in result:
    print(''.join(r))