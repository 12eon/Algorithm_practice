# 자기보다 큰 수 중 가장 오른쪽 수 출력

import sys

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
stack = []

i = 0
for i in range(n-1):
    cnt = i+1
    while cnt < n:
        if num[cnt] > n :
            print(num[cnt], end=' ')
            break
        elif cnt == n-1:
            print(-1, end=' ')
        cnt += 1

print(-1, end=' ')
