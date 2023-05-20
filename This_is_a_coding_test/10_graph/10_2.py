# 팀 결성

n,m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x

for i in range(m):
    a,b,c = map(int, input().split())
    if a == 1:
        print(parent)
        if find_parent(parent,b) == find_parent(parent,c): # parent가 아닌 find_parent로 갱신 필요
            print("YES")
        else:
            print("NO")
    else:
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    print(parent)

"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""