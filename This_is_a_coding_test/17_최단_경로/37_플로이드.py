import math

c2 = int(input())
b2 = int(input())

INF = int(1e9)

x = [[INF]*(c2+1) for _ in range(c2+1)]

for i in range(c2+1):
    x[i][i] = 0

for _ in range(b2):
    a,b,c = map(int, input().split())
    x[a][b] = min(x[a][b], c)

for k in range(1, c2+1):
    for i in range(1, c2+1):
        for j in range(1, c2+1):
            x[i][j] = min(x[i][j], x[i][k] + x[k][j])

for i in range(1, c2+1):
    for j in range(1, c2+1):
        if x[i][j] == INF:
            x[i][j] = 0
        print(x[i][j], end =' ')
    print()