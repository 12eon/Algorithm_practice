# 시간초과
import sys

m = int(sys.stdin.readline())
n = 0
num = []
for _ in range(m):
    num.append(int(sys.stdin.readline()))
    if num[-1] > n:
        n = num[-1]

d = [0]*(n+1)
for i in range(1,3):
    d[i] = i
end = [[1,0,0],[0,1,0],[1,1,1]]

for i in range(4,n+1):
    end.append([0]*3)
    for j in range(3):
        m = sum(end[j]) - end[j][2-j] # 가능한 개수
        end[-1][2-j] = m
        d[i] += m
    end.pop(0)

for m in num:
    print(d[m]%1000000009)