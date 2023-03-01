# 수가 등장한 횟수가 자기보다 큰 수중 가장 왼족에 있는 수 찾기
import sys

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
dict = {}
for i in num:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
stack = []

for i in range(n):
    if len(stack) == 0:
        stack.append(i)
    else:
        while len(stack) > 0:
            if dict[num[i]] > dict[num[stack[-1]]]:
                num[stack.pop()] = num[i]
            else:
                break
        stack.append(i)

for s in stack:
    num[s] = -1

print(' '.join([str(n) for n in num]))
