from collections import deque

n, m, v = map(int, input().split())
d = [[] for _ in range(n+1)]

for _ in range(m):
    p, q = map(int, input().split())
    d[p].append(q)
    d[q].append(p)

for e in d:
    e.sort()

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for e in d[v]:
        if not(visited[e]):
            dfs(e)

visited = [False]*(n+1)
dfs(v)
print()

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if not(visited[v]):
            visited[v] = True
            print(v, end=" ")
            for e in d[v]:
                q.append(e)

visited = [False]*(n+1)
bfs(v)