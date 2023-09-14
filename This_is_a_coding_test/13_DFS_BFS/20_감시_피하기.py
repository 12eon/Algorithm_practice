from collections import deque
import copy

n = int(input())

global qq
qq = deque([])
dx = [0,0,1,-1]
dy = [1,-1,0,0]

b = []
for i in range(n):
    b.append(list(input().split()))
    for j in range(n):
        if b[i][j] == 'T':
            for k in range(4):
                y = i+dy[k]
                x = j+dx[k]
                if x < 0 or y < 0 or x >= n or y >= n:
                    continue
                qq.append((y,x, k))

global result
result = 0

t = 0

def check(b):
    q = copy.deepcopy(qq)
    while q:
        y, x, k = q.popleft()
        if x < 0 or y < 0 or x >= n or y >= n:
            continue
        if b[y][x] == 'S':
            return
        if b[y][x] == 'X':
            q.append((y+dy[k], x+dx[k], k))
    result = 1
    print("YES")
    exit()

def seat(x, cnt, b):
    if x == cnt:
        check(copy.deepcopy(b))
        return
    for i in range(n):
        for j in range(n):
            if b[i][j] == 'X':
                b[i][j] = 'O'
                seat(x+1, cnt, b)
                b[i][j] = 'X'

seat(0, 3, b)
print("NO")