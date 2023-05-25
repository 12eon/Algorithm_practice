# 도시 분할 계획

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int, input().split())
parent = [i for i in range(n+1)]

path = []
for i in range(m):
    a,b,c = map(int, input().split())
    path.append((c,a,b))
path.sort()

result = 0
last = 0
for c,a,b in path:
    if find_parent(parent,a) != find_parent(parent,b):
        #print(a,b,result, parent)
        union_parent(parent,a,b) # 한 마을로 처리
        result += c
        last = c
print(result - last)
"""
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
"""