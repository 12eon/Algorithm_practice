n,m = map(int, input().split())
castle = []

for _ in range(n):
    castle.append([])
    values = list(input())
    for x in values:
        castle[-1].append(x)

p = [[1]*n,[1]*m]
for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            p[0][i] = 0
            p[1][j] = 0

print(max(sum(p[0]),sum(p[1])))