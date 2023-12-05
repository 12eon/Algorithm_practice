# 덩치

n = int(input())
p = []
for _ in range(n):
    x,y = map(int, input().split())
    p += [[x,y]]

looser = [1] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if p[i][0] < p[j][0] and p[i][1] < p[j][1]:
            looser[i] += 1

result = ''
for l in looser:
    result += str(l)+ ' '
print(result)