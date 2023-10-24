import sys

input = sys.stdin.readline

n, m = map(int, input().split())
x = [i for i in range(0, n+1)]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        x[b] = a
    else:
        x[a] = b

def find_parent(a):
    if x[a] != a:
        x[a] = find_parent(x[a])
    return x[a]

for _ in range(m):
    a,b = map(int, input().split())
    a = find_parent(a)
    b = find_parent(b)
    if a != b:
        union_parent(a, b)

# 전체가 최신으로 갱신!
for i in range(1, n+1):
    x[i] = find_parent(i)

print(len(set(x[1:])))