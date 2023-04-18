m,n = map(int, input().split())
d = [[] for _ in range(m+1)]
visited = [0]*(m+1) # 사이클 방지

for _ in range(n):
    v,w = map(int, input().split())
    d[v].append(w)
print(d)

result = []
for i in range(1,n+1):
    if visited[i] == 0:
        answer = []
        s = [i]
        while len(s) > 0:
            value = s.pop(0)
            for b in d[value]:
                if visited[b] == 0:
                    s.append(b)
                    answer.append(b)
                    visited[b] = 1
                else:
                    answer = []
        if len(answer) != 0:
            result.append(answer)
print(result)
max = [0,0]
for i in range(len(result)):
    if max[1] < len(result[i]):
        max = [i, len(result[i])]
r = result[max[0]]
r.sort()
for i in r:
    print(i, end=" ")