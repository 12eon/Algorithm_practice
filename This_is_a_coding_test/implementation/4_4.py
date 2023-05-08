# 게임 개발

n,m = map(int, input().split())
x,y,p = map(int, input().split())

mp = []
for _ in range(n):
    mp.append(list(map(int, input().split())))

pos = [0,3,2,1]
# 순서 : 왼쪽으로 회전
rt = [[0,-1],[1,0],[0,1],[-1,0]] # rt[pos.index(p)]

# 가본 곳 기록 0 -> 2
def check(x,y):
    order = []
    for r in rt:
        dx = x+r[1]
        dy = y+r[0]
        if dx < 0 or dx >= m or dy < 0 or dy >= n:
            continue
        if mp[dy][dx] == 0:
            order.append([dy,dx])
        else:
            order.append([])
    return order


result = 0
while 1:
    order = check(x,y)
    state = 0
    for i in range(4):
        p = (p+3)%4 # 왼쪽
        o = order[pos.index(p)]
        if len(o) > 0 and mp[o[0]][o[1]] == 0:
            state = 1
            y,x = o[0], o[1]
            mp[o[0]][o[1]] = 2
            result += 1
    if state == 0:
        value = rt[pos.index(p)]
        dy = y+value[0]
        dx = x+value[1]
        if mp[dy][dx] == 1:
            break
        x,y = dx, dy

print(result)
