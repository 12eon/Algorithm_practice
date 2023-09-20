def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]  # 갱신된 본인 반환


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


N, M = int(input()), int(input())

parent = [i for i in range(N + 1)]
for i in range(N):
    g = list(map(int, input().split()))
    for j in range(N):
        if g[j] == 1:
            union_parent(i + 1, j + 1)  # 연결

trg = list(map(int, input().split()))
st = True
for i in range(M - 1):
    if find_parent(trg[i]) != find_parent(trg[i]):
        st = False

if st:
    print("YES")
else:
    print("NO")
