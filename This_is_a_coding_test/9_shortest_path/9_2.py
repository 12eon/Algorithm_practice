# 미래 도시
import heapq

n,m = map(int, input().split()) # 회사, 경로
start = int(input())

INF = int(1e9)
g = [[INF for j in range(n+1)] for i in range(n+1)]
for i in range(1,n+1):
    g[i][i] = 0

for _ in range(m):
    a,b = map(int, input().split())
    g[a][b] = 1

# goal, dist
x,k = map(int, input().split())

for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            g[a][b] = min(g[a][b], g[a][i]+g[i][b])

dist = INF
for i in range(1,n+1):
    value = g[k][i] + g[i][x]
    if value < dist:
        dist = value
if g[1][k] < INF and g[k][x] < INF and dist < INF:
    print(dist)
else:
    print(-1)