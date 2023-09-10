# board 최대 크기와 반복 횟수가 작으면, 전체 조회
# board 최대 크기와 반복 횟수가 작으면, 전체 조회

import copy

h, w = map(int, input().split())
box = []
for j in range(h):
    box.append(list(map(int, input().split())))
    for i in box[-1]:
        if box[j][i] == 2:

print(box)

total = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def count_block():
    global total
    virus = copy.deepcopy(box)
    v = []
    for i in range(h):
        for j in range(w):
            if tmp_graph[i][j] == 2:
                q.append((i, j))

    while v:
        now = v.pop()
        for i in range(4):
            y = dy[i] + now[0]
            x = dx[i] + now[1]
            if x < 0 or y < 0 or x >= w or y >= h:
                continue
            if box[y][x] != 1:
                box[y][x] = 2
                virus.append([y,x])
    c = 0
    for t in range(h):
        c += virus[t].count(0)
    if total < c:
        total = c

def put_stick(cnt):
    if cnt == 0:
        count_block()
    for y in range(h):
        for x in range(w):
            if box[y][x] == 0:
                box[y][x] = 1
                put_stick(cnt-1)
                box[y][x] = 0
put_stick(3)
print(total)