def find(x): # 가장 위의 부모 찾기
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y: # 다른 그룹
        parent[y] = x  # x를 y의 부모로 처리
        number[x] += number[y] # 그룹의 원소 수 합

case = int(input())

for _ in range(case):
    parent = dict()
    number = dict()
    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x,y)
        print(number[find(x)])
