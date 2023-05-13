# 다익스트라 알고리즘

n,m = map(int, input().split())
start = int(input())

g = [[] for i in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    g[a].append([b,c])

INF = int(1e9)
d = [INF]*(n+1)
v = [0]*(n+1)

def find_next():
    value = INF
    index = 0
    for i in range(1, n+1):
        if d[i] < value and v[i] == 0:
            index = i
            value = d[i]
    return index

def dijkstra(start):
    v[start] = 1
    d[start] = 0
    for j in g[start]:
        d[j[0]]= j[1] # 현재 각 인덱스 까지 거리
    #print(d)

    for i in range(n-1): # 처리 필요한 노드 수
        now = find_next()
        v[now] = 1 # 방문
        for j in g[now]: # 비용
            cost = d[now]+j[1]
            if cost < d[j[0]]:
                d[j[0]] = cost
        #print(d)

dijkstra(start)

for i in d[1:]:
    if i == INF:
        print("INFINITY")
    else:
        print(i)