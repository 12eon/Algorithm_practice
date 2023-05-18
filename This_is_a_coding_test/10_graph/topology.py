# 위상 정렬
from collections import deque

v,e = map(int, input().split())
visited = [0]*(v+1)
cnt = [0]*(v+1)
d = [[] for i in range(v+1)]
result = []
for _ in range(e):
    a,b = map(int, input().split())
    d[a].append(b)
    cnt[b] += 1 # 도착하는 경우 = 0 -> 시작 노드

q = deque([])
i = cnt[1:].index(0) + 1
print(cnt, i)
q.append(i)
visited[i] = 1
result = []

while q:
    value = q.popleft()
    #print(value, q)
    result.append(value)
    for i in d[value]:
        if visited[i] == 0:
            visited[i] = 1
            q.append(i)

for i in result:
    print(i, end=" ")
