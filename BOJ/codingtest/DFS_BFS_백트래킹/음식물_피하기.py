from collections import deque
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

b = [[0]*m for _ in range(n)]
num = []
for _ in range(k):
    y,x = map(int, input().split())
    num.append([y-1,x-1])
    b[y-1][x-1] = 1


def bfs(y,x):
    global total
    q = deque([[y,x,1]])

    while q:
        ny, nx, nv = q.popleft()
        total += 1 # 연관된 호출

        for i in range(4):
            y = dy[i] + ny
            x = dx[i] + nx

            if 0 <= y < n and 0 <= x < m and b[y][x] == 1:
                b[y][x] = 0
                q.append([y, x, nv + 1])

result = 1
for i in num:
    y,x = i
    if b[y][x] == 1:
        b[y][x] = 0 # 시작 지점도 처리
        total = 0
        bfs(y, x)
        result = max(result, total)

print(result)