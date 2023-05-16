# 크루스칼 알고리즘 : 최단거리 순으로 사이클 없게 모두 연결

v,e = map(int, input().split())

INF = int(1e9)
d = []

for i in range(e):
    a,b,c = map(int, input().split())
    d.append((a,b,c))
d.sort(key = lambda x : x[2])


def find_parent(parent, x):
    if result[x] == x:
        return result[x]
    find_parent(parent, result[x])

result = [i for i in range(v+1)]
value = []
for a,b,c in d:
    if len(value) == v:
        break
    if result[a] == result[b]:
        continue

    a = find_parent(result, a)
    b = find_parent(result, b)
    if a < b:
        result[b] = a
    else:
        result[a] = b

print(result)
print(value)
print(sum(value))