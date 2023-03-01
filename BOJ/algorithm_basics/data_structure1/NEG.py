# 자기보다 큰 수 중 가장 오른쪽 수 출력
# = 인덱스 0부터 왼쪽 인덱스 값들이 자기보다 작으면 덮게

import sys

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
stack = []

for i in range(n):
    if len(stack) == 0:
        stack.append(i) # 인덱스
    else: # stack에는 자기보다 작은 인덱스들이 들어있음
        while len(stack) != 0:
            if num[i] > num[stack[-1]]:
                num[stack.pop()] = num[i]
            else:
                break
        stack.append(i)
for s in stack:
    num[s] = -1

print(' '.join([str(n) for n in num]))
