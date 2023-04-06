n,s,m = map(int, input().split())
num = list(map(int, input().split()))

cmp = [[0] * (m + 1) for _ in range(n + 1)]
cmp[0][s] = 1
for i in range(1, n + 1):
    for j in range(m + 1):
        if cmp[i - 1][j] == 0:
            continue
        if j - num[i - 1] >= 0:
            cmp[i][j - num[i - 1]] = 1
        if j + num[i - 1] <= m:
            cmp[i][j + num[i - 1]] = 1

result = -1

for i in range(m, -1, -1):
    if cmp[n][i] == 1:
        result = i
        break
