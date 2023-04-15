import sys
sys.setrecursionlimit(100000) # RecursionError 해결

cnt = int(input())

def check(i,j):
    if i > 0:
        if d[i-1][j] == 1:
            d[i-1][j] = 0
            check(i-1, j)
    if i < n-1:
        if d[i+1][j] == 1:
            d[i+1][j] = 0
            check(i+1, j)
    if j > 0:
        if d[i][j-1] == 1:
            d[i][j-1] = 0
            check(i, j-1)
    if j < m-1:
        if d[i][j+1] == 1:
            d[i][j+1] = 0
            check(i, j+1)

for _ in range(cnt):
    m,n,k = map(int, input().split())

    d = [[0]*m for _ in range(n)]
    for _ in range(k):
        v,w = map(int, input().split())
        d[w][v] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if d[i][j] == 1:
                d[i][j] = 0
                result += 1
                check(i,j)
    print(result)