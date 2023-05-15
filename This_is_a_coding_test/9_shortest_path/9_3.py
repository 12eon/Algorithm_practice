# 미래 도시 -> 최단 거리 문제
import heapq

n,m,c = map(int, input().split()) # 도시, 통로, 시작 도시

INF = int(1e9)
g = [[INF for j in range(n+1)] for i in range(n+1)]
for i in range(1,n+1):
    g[i][i] = 0

for _ in range(m):
    a,b,v = map(int, input().split())
    g[a][b] = v

"""for i in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            g[a][b] = min(g[a][b], g[a][i]+g[i][b])"""

d = [INF]*(n+1) # 최단거리
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start)) # 거리, 인덱스
    d[start] = 0

    while q:
        dist, now = heapq.heappop()
        if d[now] < dist: # 처리함
            continue


dijkstra(start)

result = [-1,0] # 시작 위치 제거
for i in range(1,n+1):
    if d[i] < INF:
        result[0] += 1
        result[1] = max(d[i], result[1])
print(result[0], result[1])