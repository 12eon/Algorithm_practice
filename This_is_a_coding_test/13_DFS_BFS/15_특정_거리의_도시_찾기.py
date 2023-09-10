# 모든 길이가 동일 할 때는 bfs

from collections import deque
import sys

f = sys.stdin.readline
n, m, k, x = map(int, f().split())

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [-1] * (n+1)
distance[x] = 0 # 시작

for _ in range(m):
    a, b = map(int, f().split())
    graph[a].append(b)

q = deque([x])
while q:
    v = q.popleft()
    if visited[v] == False:
        visited[v] = True
        for i in graph[v]:
            if distance[i] == -1: # 이전 값 없는 경우 = 처음 연결
                distance[i] = distance[v]+j
                q.append(i)

if k in distance:
    for i in range(1, n+1):
        if distance[i] == k:
          print(i)
else:
  print(-1)