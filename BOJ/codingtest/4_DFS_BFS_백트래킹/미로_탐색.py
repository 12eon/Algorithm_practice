import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
check = []
for _ in range(n):
    check.append(list(input().rstrip()))
dy = [-1,1,0,0]
dx = [0,0,1,-1]

def bfs(sy, sx):
    q = deque([(sy,sx,1)]) # 거리 추가

    while q:
        v = q.popleft()
        if v[0] == n-1 and v[1] == m-1:
            return v[2]

        for i in range(4):
            y = v[0] + dy[i]
            x = v[1] + dx[i]
            if 0 <= y < n and 0 <= x < m and check[y][x] == '1':
                check[y][x] = '0'
                q.append((y,x, v[2]+1))
print(bfs(0,0))