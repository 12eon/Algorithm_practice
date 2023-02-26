import sys

n, m = map(int, sys.stdin.readline().split())
num = [i for i in range(1, n+1)]
i = 0
result = []

for _ in range(n):
    i += m-1
    if i >= len(num):
        i %= len(num) # 삭제로 인한
    result.append(num.pop(i))

print('<'+', '.join(map(str, result))+'>')