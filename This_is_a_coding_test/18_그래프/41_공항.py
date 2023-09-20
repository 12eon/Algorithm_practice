# https://www.acmicpc.net/problem/10775

G, P = int(input()), int(input())
parent = [i for i in range(G+1)]

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]  # 갱신된 본인 반환


def union_parent(a, b):
    a = find_parent(a) # gate에 남은 자리 개수
    b = find_parent(b)
    # 남은 자리의 수 갱신
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

total = 0
for _ in range(P):
    p = find_parent(int(input())) # 자리가 있는지
    if p == 0:
        break
    union_parent(p, p-1) # 내 자리 대신, 빈 앞쪽 gate에 정차
    total += 1
print(total)