n = int(input())
g = 1
while n != 0:
    p = 0
    m = []
    result = []
    for j in range(n):
        v = list(input().split())
        m.append([v[0]])
        length = len(v)
        for i in range(1, length):
            if v[i] == 'N':
                p = 1
                m[-1].append((n+j-i)%n) # 이름 인덱스 위치

    print("Group", g)
    g += 1
    for i in range(n):
        name = m[i][0]
        for j in m[i][1:]:
            print(m[j][0],"was nasty about",name)
    if p == 0:
        print("Nobody was nasty")
    print()
    n = int(input())
