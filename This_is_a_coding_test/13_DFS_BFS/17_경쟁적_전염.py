h,w = map(int, input().split())
b = []
for _ in range(h):
    b.append(list(map(int, input().split())))

d = dict([])
d[1] = []
d[2] = []
d[3] = []
for y in range(h):
    for x in range(w):
        if b[y][x] != 0:
            d[b[y][x]].append([y,x])

s, x, y = map(int, input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for c in range(s):
    for i in range(1,4):
        for n, m in d[i]:
            for j in range(4):
                nx = dx[j] + m
                ny = dy[j] + n
                if nx < 0 or ny < 0 or nx >= w or ny >= h:
                    continue
                if b[ny][nx] == 0:
                    b[ny][nx] = i
        #print(b)
print(b[x-1][y-1])