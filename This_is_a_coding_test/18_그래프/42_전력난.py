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


while True:
    M, N = map(int, input().split())
    if M == 0 and N == 0:
        break

    parent = list(range(M))
    graph = [list(map(int, input().split())) for i in range(N)]
    graph.sort(key=lambda x: x[2])

    cost = 0
    for edge in graph:
        if find_p(edge[0]) != find_p(edge[1]):
            comb_p(edge[0], edge[1]) # 도로 설치
        else:
            cost += edge[2] # 절약할 수 있는 최대 액수
    print(cost)