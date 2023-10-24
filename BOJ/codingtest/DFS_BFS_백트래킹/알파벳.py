import sys

input = sys.stdin.readline
n, m = map(int, input().split())
alpha = [list(map(str, input().strip())) for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,1,-1]
total = 1

def bfs(sy, sx):
    global total
    q = set([(sy, sx, alpha[0][0])]) # 돌아서 두번 방문 못하게 (백트리킹 대신 set)

    while q:
        sy,sx,v = q.pop()
        total = max(total, len(v))

        for i in range(4):
            y = dy[i] + sy
            x = dx[i] + sx

            if 0 <= y < n and 0 <= x < m and alpha[y][x] not in v:
                q.add((y,x, v + alpha[y][x]))

bfs(0,0)
print(total)