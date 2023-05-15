# 개선된 다익스트라 알고리즘
import heapq

n,m = map(int, input().split())
start = int(input())

g = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    g[a].append([b,c])

INF = int(1e9)
d = [INF]*(n+1)
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start)) # 거리, 인덱스
    d[start] = 0

    while q:
        dist, now = heapq.heappop()
        if d[now] < dist: # 처리함
            continue
        for j in g[now]: # 현재 노드 거쳐서 가는 경우
            cost = d[now]+j[1] # start~자신 + 자신~상대
            if cost < d[j[0]]:
                d[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(start)

for i in d[1:]:
    if i == INF:
        print("INFINITY")
    else:
        print(i)