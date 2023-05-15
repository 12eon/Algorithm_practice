# 서로소 집합 : 부모(작은수) 인덱스 가지기


v,e = map(int, input().split())

parent = [0]*(v+1)
for p in range(1,v+1):
    parent[p] = p

for find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x

for union_parent(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 결과
cycle = 0
for i in range(e):
    a,b = map(int, input().split())
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if x == y:
        cycle = 1
        break
    else:
        union_parent(parent, a, b) # 2개 원소가 속한 집합(가장 작은 인덱스)
if cycle == 1:
    print("cycle")
else:
    print("None")

# 사이클 없는 경우, 결과
"""
for i in range(e):
    print(find_parent(parent, i), end=" ")
print()
for i in range(e):
    print(parent[i], end=" ")"""