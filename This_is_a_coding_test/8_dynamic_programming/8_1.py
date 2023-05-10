# 개미 전사 : 각 단계까지 최고 max 값 누적

n = int(input())
box = list(map(int, input().split()))

v = [0]*(n)
v[0] = b[0]
v[1] = b[1]
v[2] = b[2]

for i in range(3, n):
    v[i] = max(v[i-2], v[i-1])
print(v[n-1])