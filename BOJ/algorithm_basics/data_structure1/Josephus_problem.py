# 시간 초과
import sys

n, m = map(int, sys.stdin.readline().split())
q2 = list(range(n,0,-1))
q1 = list()

i = 0
std = 0
result = []
while len(result) < n-1:
    if len(q2) == 0:
        q1.reverse()
        q1, q2 = q2, q1
    if std == m-1:
        result.append(q2.pop())
        std = 0
        #print('r : ', result)
    else:
        q1.append(q2.pop())
        std += 1
q1 = q1+q2
print('<', end='')
for r in result:
    print(str(r)+',', end=' ')
print(str(q1[0])+'>', end='')