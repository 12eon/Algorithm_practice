from collections import deque
import sys

input = sys.stdin.readline
dy = [2,2,-2,-2, -1,1,-1,1]
dx = [-1,1,-1,1, 2,2,-2,-2]

def bfs():
    q = deque([[sy,sx,0]])

    while q:
        ny, nx, nv = q.popleft()

        if ny == ey and nx == ex:
            return nv

        for i in range(8):
            y = dy[i] + ny
            x = dx[i] + nx

            if 0 <= y < n and 0 <= x < n and vst[y][x] == 0:
                vst[y][x] = 1
                q.append([y, x, nv + 1])

t = int(input())
for _ in range(t):
    n = int(input())
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())
    vst = [[0]*n for _ in range(n)]
    print(bfs())
