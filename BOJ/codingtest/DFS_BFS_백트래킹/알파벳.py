import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
alpha = []
for _ in range(n):
    alpha.append(list(input().rstrip()))
print(alpha)
check = [[0]*m for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,1,-1]

def dfs(sy, sx, cand):
    for i in range(4):
        y = sy + dy[i]
        x = sx + dx[i]
        if 0 <= y < n and 0 <= x < m and alpha[y, x] not in cand:
            return 1 + dfs(y, x, cand + alpha[y, x])
        return 0

result = 0
for i in range(m):
    x = dfs(0,m, [alpha[0][i]])
    print(x)
    result = max(result, x)

print(result)