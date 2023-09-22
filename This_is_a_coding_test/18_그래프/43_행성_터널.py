
def find_p(x):
    if x != parent[x]:
        parent[x] = find_p(parent[x])
    return parent[x]


def comb_p(a, b):
    a = find_p(a)
    b = find_p(b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

import sys

N = int(sys.stdin.readline())
x = []
y = []
z = []
for i in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))
x.sort()
y.sort()
z.sort()
graph = []
for i in range(N-1):  # 메모리 초과 해결 -> 총 N-1개 탐색 => 각 행마다 최대가 N-1개 가능
    graph.append((x[i+1][0]-x[i][0], x[i][1], x[i+1][1]))
    graph.append((y[i+1][0]-y[i][0], y[i][1], y[i+1][1]))
    graph.append((z[i+1][0]-z[i][0], z[i][1], z[i+1][1]))
graph.sort()

parent = list(range(N+1))
total = 0
for p,i,j in graph:
    if find_p(i) != find_p(j):
        comb_p(i,j)
        total += p

print(total)
