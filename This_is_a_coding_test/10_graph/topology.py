# 위상 정렬
import deque

v,e = map(int, input().split())

INF = int(1e9)
v = [0]*(v+1)
d = [[]*(v+1)]
for _ in e:
    a,b = map(int, input().split())
    d[a].append(b)

cnt = 1
v[1] = 1
q = deque([])
for i in d[1]:
    q.append(i)

while q:
    value = q.popleft()
    v[value[0]] = cnt
    cnt += 1
    for i in d[value[1]]:
        if i[0] == 0:
            q.append(i)

print(v)
