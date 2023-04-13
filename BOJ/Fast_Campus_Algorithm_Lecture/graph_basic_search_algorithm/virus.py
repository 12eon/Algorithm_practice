cnt = int(input())
n = int(input())

d = [[] for _ in range(cnt+1)]
for _ in range(n):
    v,w = map(int, input().split())
    d[w] += [v]
    d[v] += [w]

result = 0
cmp = [0]*(cnt+1)
def calc(v):
    global result
    result += 1
    cmp[v] = 1
    for w in d[v]:
        if cmp[w] == 0:
            calc(w)
calc(1)
print(result-1)