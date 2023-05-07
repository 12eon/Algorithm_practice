# 음료수 얼려먹기 -> 연결이 끊어진 개수

from collections import deque

n,m = map(int, input().split())
ice = []
v = [] # visited 판단
for j in range(n):
    ice.append([int(x) for x in list(input().rstrip())])
    for i in range(m):
        if ice[-1][i] == 0:
            v.append([j,i])
s = [0]*len(v)

box = [[1,0],[-1,0],[0,1],[0,-1]]
def check():
    global s
    global q
    while q:
        value = q.popleft()
        #print(value)
        for b in box:
            dy = value[0] + b[0]
            dx = value[1] + b[1]
            if dy < 0 or dy >= n or dx < 0 or dx >= m:
                continue
            if ice[dy][dx] == 0:
                ice[dy][dx] = 2
                q.append([dy,dx])
                s[v.index([dy,dx])] = 1

result = 0
q = deque([])
i = 0
while i < len(s):
    if s[i] == 0:
        q.append(v[i])
        # 방문
        s[i] = 1
        ice[v[i][0]][v[i][1]] = 2
        check()
        result += 1
    i += 1
print(result)