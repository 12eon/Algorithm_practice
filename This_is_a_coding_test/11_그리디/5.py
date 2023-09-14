# 볼링공 고르기 -> 조합

m,n = map(int, input().split())
values = list(map(int, input().split()))

v = [0]*(n+1)
for i in values:
    v[i] += 1
cnt = n+1 - v.count(0)

total = 0
for i in range(1, n):
    if v[i] == 0:
        continue
    for j in range(i+1, n+1):
        if v[j] != 0:
            total += v[i]*v[j]
print(total)