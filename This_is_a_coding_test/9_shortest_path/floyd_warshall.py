# 플로이드 워셜 알고리즘

n = int(input())
m = int(input())

INF = int(1e9)
g = [[INF for j in range(n+1)] for i in range(n+1)]
for i in range(1,n+1):
    g[i][i] = 0 # 자신

for _ in range(m):
    a,b,c = map(int, input().split())
    g[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            g[a][b] = min(g[a][b], g[a][k] + g[k][b])


for i in range(1, n+1):
    for j in range(1, n+1):
        if i == INF:
            print("INFINITY", end=" ")
        else:
            print(i, end=" ")
    print()