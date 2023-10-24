from collections import deque
import sys

input = sys.stdin.readline

def check_line(ny, nx):
    for v in vst:
        if v == nx:
            return 0
    i = 0
    while i < n:
        if vst[i] != -1 and abs(ny-i) == abs(nx-vst[i]):
            return 0
        i += 1
    return 1

def queen(y):
    if y == n:
        global total
        total += 1
        return

    for x in range(n):
        if check_line(y, x) == 1:
            vst[y] = x
            queen(y+1)
            vst[y] = -1

n = int(input())
vst = [-1 for _ in range(n)]
total = 0
queen(0)
print(total)
